from .models import depa

def get_depts(request):
    all_depas = depa.objects.all()
    return {
        'depas': all_depas
    }
