from django.db import models

from django.core.exceptions import ObjectDoesNotExist


class ReferenceManager(models.Manager):

    def filter_crf_for_visit(self, model=None, visit=None):
        return self.filter(
            identifier=visit.subject_identifier,
            model=model,
            report_datetime=visit.report_datetime,
            timepoint=visit.visit_code)

    def get_crf_for_visit(self, model=None, visit=None, field_name=None):
        try:
            model_obj = self.get(
                identifier=visit.subject_identifier,
                model=model,
                report_datetime=visit.report_datetime,
                timepoint=visit.visit_code,
                field_name=field_name)
        except ObjectDoesNotExist:
            model_obj = None
        return model_obj

    def get_requisition_for_visit(self, model=None, visit=None, panel_name=None):
        try:
            model_obj = self.get(
                identifier=visit.subject_identifier,
                model=model,
                report_datetime=visit.report_datetime,
                timepoint=visit.visit_code,
                field_name='panel_name',
                value_str=panel_name)
        except ObjectDoesNotExist:
            model_obj = None
        return model_obj
