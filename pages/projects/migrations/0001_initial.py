# Generated by Django 2.0.8 on 2018-11-15 16:04

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.CharField(blank=True, max_length=1000)),
                ('icon', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('project_url', models.CharField(blank=True, max_length=250)),
                ('intro', models.CharField(blank=True, max_length=250)),
                ('body', wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('html_block', wagtail.core.blocks.RawHTMLBlock()), ('document_block', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, verbose_name='Page body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='projects.ProjectPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='projects.ProjectPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_projectpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='projectpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='projects.ProjectPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
