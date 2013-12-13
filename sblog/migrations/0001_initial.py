# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('email', models.EmailField(max_length=75, blank=True),), ('website', models.URLField(blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Author',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('tag_name', models.CharField(max_length=20, blank=True),), ('create_time', models.DateTimeField(auto_now_add=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Tag',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('caption', models.CharField(max_length=50),), ('author', models.ForeignKey(to=u'sblog.Author', to_field=u'id'),), ('content', models.TextField(),), ('publish_time', models.DateTimeField(auto_now_add=True),), ('update_time', models.DateTimeField(auto_now=True),), ('tags', models.ManyToManyField(to=u'sblog.Tag', blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Blog',
        ),
    ]
