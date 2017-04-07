from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        from subprocess import call
        call("psql -h nshenoy.com -d hpe -U admin -W -c \"copy dashboard_server from STDIN with delimiter as ','\" < perform-csv/perform-summary.csv \"HEADER\"")
