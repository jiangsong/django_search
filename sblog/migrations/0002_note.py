# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('sblog', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('user', models.ForeignKey(to=u'sblog.Author', to_field=u'id'),), ('pub_date', models.DateTimeField(),), ('title', models.CharField(max_length=200),), ('body', models.TextField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Note',
        ),
    ]
