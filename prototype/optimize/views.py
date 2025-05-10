# from django.shortcuts import render

# def upload_view(request):
#     return render(request, 'upload.html')
from django.shortcuts import render

def home(request):
    return render(request, 'upload.html')

def result(request):
    if request.method == 'POST':
        use_case = request.POST['use_case']
        performance = request.POST['performance']
        power = request.POST['power']
        area = request.POST['area']
        node = request.POST['node']

        # Dummy logic
        output = {
            "core": "RISC-V (Low Power)",
            "memory": "512KB SRAM",
            "connectivity": "BLE",
            "ppa": {
                "power": f"{power}mW estimated",
                "area": f"{area}mm² estimated",
                "performance": performance
            }
        }
        return render(request, 'result.html', {'output': output})

    return render(request, 'upload.html')
