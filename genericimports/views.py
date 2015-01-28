# -*- coding: utf-8 -*-

import logging
import os

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

import django_rq

from .parser import Importer
from .forms import ReportForm
from .models import Report

logger = logging.getLogger(__name__)


def trigger_queue(obj_id, file, querystrings):

    """Starts the queue task

    For some reason django-rq doesn't support calling methods inside classes
    so we have to trigger the process with this.
    """
    Importer(obj_id, file, querystrings)


@staff_member_required
def import_file(request):

    """Import a CSV or XLS file into the database.

    This view will create a report with the uploaded file and the email address
    especified on the form, then it will save the querystrings (if any) and
    get the full path to the uploaded file. After that we just queue the
    processing task with django-rq.

    Args:
        request: The main request

    Returns:
        A template confirming that the task has been queued
    """
    form = ReportForm(request.POST, request.FILES)
    if request.method == 'POST':
        try:
            # Get the required fields
            report_email = request.POST.get("email", '')
            report_file = request.FILES['file']
            # Save the data
            report = Report(email=report_email, original_file=report_file)
            report.save()
            # Get the query strings
            querystrings = request.META['QUERY_STRING']
            # Start the task queue
            queue = django_rq.get_queue('importer')
            queue.enqueue(trigger_queue, args=(report.id, report.original_file.name, querystrings))
            return render_to_response('thanks.html')
        except Exception as e:
            logger.error("CRITICAL ERROR: THE TASK COULDN'T BE EXECUTED.")
            logger.error(e)
            return render_to_response('error.html')
    else:
        return render_to_response('import.html', {'form': form},
                                  context_instance=RequestContext(request))


def list_reports(request):

    """
    List all the reports for the performed imports.
    """
    pass
