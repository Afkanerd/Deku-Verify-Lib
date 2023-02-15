"""Peewee Deku Verify Sessions Model"""

from datetime import datetime, timedelta
from uuid import uuid4
import random

from peewee import Model, CharField, DateTimeField, IntegerField

from DekuVerify.schemas.connector import db

random_4_digit = random.randint(1000, 9999)
default_code_lifetime = str(datetime.now()) + timedelta(minutes=10)

class DekuVerifySessions(Model):
    """Model definition"""
    sid = CharField(primary_key=True, default=uuid4)
    code = CharField(default=random_4_digit)
    expires = DateTimeField(null=True, default=default_code_lifetime)
    status = CharField(null=True, default="pending")
    verified_attempts = IntegerField(default=0)
    sent_attempts = IntegerField(default=0)
    created_on = DateTimeField(null=True, default=datetime.now)

    class Meta:
        """Meta definition"""
        database = db
        table_name = "deku_verify_sessions"

if not db.table_exists('deku_verify_sessions'):
    db.create_tables([DekuVerifySessions])
