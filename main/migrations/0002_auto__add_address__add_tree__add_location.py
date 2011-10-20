# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('main_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('main', ['Address'])

        # Adding model 'Tree'
        db.create_table('main_tree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('scientific_name', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('variety', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')(default=None, null=True)),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('condition', self.gf('django.db.models.fields.PositiveIntegerField')(default=None, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django_fsm.db.fields.fsmfield.FSMField')(default='unverified', max_length=50, db_index=True)),
            ('submitted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitted_trees_set', null=True, to=orm['auth.User'])),
            ('user_steward_choice', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('main', ['Tree'])

        # Adding M2M table for field stewards on 'Tree'
        db.create_table('main_tree_stewards', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tree', models.ForeignKey(orm['main.tree'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('main_tree_stewards', ['tree_id', 'user_id'])

        # Adding model 'Location'
        db.create_table('main_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geolocation', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=3857, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Address'])),
        ))
        db.send_create_signal('main', ['Location'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('main_address')

        # Deleting model 'Tree'
        db.delete_table('main_tree')

        # Removing M2M table for field stewards on 'Tree'
        db.delete_table('main_tree_stewards')

        # Deleting model 'Location'
        db.delete_table('main_location')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.address': {
            'Meta': {'object_name': 'Address'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        'main.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Address']"}),
            'geolocation': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.tree': {
            'Meta': {'object_name': 'Tree'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'condition': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'status': ('django_fsm.db.fields.fsmfield.FSMField', [], {'default': "'unverified'", 'max_length': '50', 'db_index': 'True'}),
            'stewards': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trees_stewarded_set'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'submitted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submitted_trees_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_steward_choice': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'variety': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']
