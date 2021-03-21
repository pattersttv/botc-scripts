import django_tables2 as tables
from .models import Script, ScriptVersion

class ScriptTable(tables.Table):
    class Meta:
        model = ScriptVersion
        exclude = ('id','content','script')
        sequence = ('name', 'type', 'version', 'author', 'json', 'pdf')

    name = tables.Column(empty_values=(), order_by='script.name')
    author = tables.Column()
    version = tables.Column()
    json = tables.Column(orderable=False)
    pdf = tables.Column(orderable=False)

    def render_name(self, value, record):
        return record.script.name

    def render_type(self, value, record):
        return record.type
