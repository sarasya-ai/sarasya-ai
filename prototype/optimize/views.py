from django.shortcuts import render
from .models import ChipDesign

def optimize_chip(request):
    try:
        if request.method == 'POST':
            performance = request.POST.get('performance')
            max_power = int(request.POST.get('max_power'))
            max_area = int(request.POST.get('max_area'))

            # Define component options
            cores = {
                'Low': {'name': 'RISC-V Low Power', 'power': 10, 'area': 5},
                'Balanced': {'name': 'ARM Cortex-A53', 'power': 70, 'area': 15},
                'High': {'name': 'ARM Cortex-A78', 'power': 100, 'area': 20}
            }

            memories = {
                '128KB SRAM': {'power': 10, 'area': 5},
                '256KB SRAM': {'power': 20, 'area': 10},
                '1MB SRAM': {'power': 40, 'area': 20}
            }

            connectivities = {
                'BLE': {'power': 10, 'area': 3},
                'WiFi': {'power': 30, 'area': 7},
                '5G': {'power': 60, 'area': 12}
            }

            result = None

            for mem, mem_vals in memories.items():
                for conn, conn_vals in connectivities.items():
                    total_power = cores[performance]['power'] + mem_vals['power'] + conn_vals['power']
                    total_area = cores[performance]['area'] + mem_vals['area'] + conn_vals['area']

                    if total_power <= max_power and total_area <= max_area:
                        result = {
                            'performance': performance,
                            'core': cores[performance]['name'],
                            'memory': mem,
                            'connectivity': conn,
                            'total_power': total_power,
                            'total_area': total_area
                        }


                        # Save to DB
                        ChipDesign.objects.create(
                            performance=performance,
                            max_power=max_power,
                            max_area=max_area,
                            selected_core=cores[performance]['name'],
                            selected_memory=mem,
                            selected_connectivity=conn,
                            total_power=total_power,
                            total_area=total_area
                        )
                        break
                if result:
                    break

            return render(request, 'results.html', {'result': result})
        
        return render(request, 'upload.html')
    except Exception as e:
        return render(request, 'results.html', {'error': str(e)})
