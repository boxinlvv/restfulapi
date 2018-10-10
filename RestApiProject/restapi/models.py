#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

class Student(models.Model):
    name = models.CharField(u'姓名', max_length=100)
    sex = models.CharField(u'性别', max_length=50)
    sid = models.CharField(u'学号', max_length=100)

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)