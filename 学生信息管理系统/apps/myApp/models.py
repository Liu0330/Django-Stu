from django.db import models


# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    gteacher = models.CharField(max_length=20)
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sminzu = models.CharField(max_length=20)
    sbir = models.IntegerField()
    scontend = models.CharField(max_length=20)
    shome = models.CharField(max_length=20)
    sidcard = models.CharField(max_length=20)
    sschnum = models.IntegerField()
    stel = models.CharField(max_length=20)
    steacher = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    # 关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    def __str__(self):
        return self.sname




class Score(models.Model):
    name = models.CharField(max_length=20,default=None)
    math = models.IntegerField()
    chinese = models.IntegerField()
    english = models.IntegerField()

    def __str__(self):
        return self.name

    # 关联外键
    students = models.ForeignKey("Students", on_delete=models.CASCADE)



from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('moniter', u"Moniter"),
    ('lvs', u"LVS"),
    ('db', u"Database"),
    ('analysis', u"Analysis"),
    ('admin', u"Admin"),
    ('storge', u"Storge"),
    ('web', u"WEB"),
    ('email', u"Email"),
    ('mix', u"Mix"),
)


@python_2_unicode_compatible
class AccessRecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = u"Access Record"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return "%s Access Record" % self.date.strftime('%Y-%m-%d')








#
# @python_2_unicode_compatible
# class IDC(models.Model):
#     name = models.CharField(max_length=64)
#     description = models.TextField()
#
#     contact = models.CharField(max_length=32)
#     telphone = models.CharField(max_length=32)
#     address = models.CharField(max_length=128)
#     customer_id = models.CharField(max_length=128)
#     groups = models.ManyToManyField(Group)  # many
#
#     create_time = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = u"IDC"
#         verbose_name_plural = verbose_name
#
#
# @python_2_unicode_compatible
# class Host(models.Model):
#     idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
#     name = models.CharField(max_length=64)
#     nagios_name = models.CharField(u"Nagios Host ID", max_length=64, blank=True, null=True)
#     ip = models.GenericIPAddressField(blank=True, null=True)
#     internal_ip = models.GenericIPAddressField(blank=True, null=True)
#     user = models.CharField(max_length=64)
#     password = models.CharField(max_length=128)
#     ssh_port = models.IntegerField(blank=True, null=True)
#     status = models.SmallIntegerField(choices=SERVER_STATUS)
#
#     brand = models.CharField(max_length=64, choices=[(i, i) for i in (u"DELL", u"HP", u"Other")])
#     model = models.CharField(max_length=64)
#     cpu = models.CharField(max_length=64)
#     core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
#     hard_disk = models.IntegerField()
#     memory = models.IntegerField()
#
#     system = models.CharField(u"System OS", max_length=32, choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")])
#     system_version = models.CharField(max_length=32)
#     system_arch = models.CharField(max_length=32, choices=[(i, i) for i in (u"x86_64", u"i386")])
#
#     create_time = models.DateField()
#     guarantee_date = models.DateField()
#     service_type = models.CharField(max_length=32, choices=SERVICE_TYPES)
#     description = models.TextField()
#
#     administrator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Admin")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = u"Host"
#         verbose_name_plural = verbose_name
#
#
# @python_2_unicode_compatible
# class MaintainLog(models.Model):
#     host = models.ForeignKey(Host, on_delete=models.CASCADE)
#     maintain_type = models.CharField(max_length=32)
#     hard_type = models.CharField(max_length=16)
#     time = models.DateTimeField()
#     operator = models.CharField(max_length=16)
#     note = models.TextField()
#
#     def __str__(self):
#         return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
#                                                self.maintain_type, self.hard_type)
#
#     class Meta:
#         verbose_name = u"Maintain Log"
#         verbose_name_plural = verbose_name
#
#
# @python_2_unicode_compatible
# class HostGroup(models.Model):
#     name = models.CharField(max_length=32)
#     description = models.TextField()
#     hosts = models.ManyToManyField(
#         Host, verbose_name=u'Hosts', blank=True, related_name='groups')
#
#     class Meta:
#         verbose_name = u"Host Group"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
