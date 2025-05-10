from django.shortcuts import render

# Sample component library
components = {
    "cores": [
        {"name": "RISC-V Low Power", "performance": "Low", "power": 10, "area": 5},
        {"name": "RISC-V High Perf", "performance": "High", "power": 100, "area": 20},
        {"name": "ARM Cortex-A53", "performance": "Balanced", "power": 70, "area": 15},
    ],
    "memory": [
        {"name": "256KB SRAM", "power": 20, "area": 10},
        {"name": "1MB SRAM", "power": 40, "area": 20},
    ],
    "connectivity": [
        {"name": "WiFi", "power": 30, "area": 8},
        {"name": "BLE", "power": 10, "area": 3},
    ]
}

def optimize_chip(request):
    if request.method == "POST":
        perf = request.POST.get("performance")
        max_power = int(request.POST.get("power"))
        max_area = int(request.POST.get("area"))

        selected = {"core": None, "memory": None, "connectivity": None}
        total_power = 0
        total_area = 0

        # Pick core
        for core in components["cores"]:
            if core["performance"] == perf:
                if core["power"] <= max_power and core["area"] <= max_area:
                    selected["core"] = core
                    total_power += core["power"]
                    total_area += core["area"]
                    break

        # Memory
        for mem in components["memory"]:
            if total_power + mem["power"] <= max_power and total_area + mem["area"] <= max_area:
                selected["memory"] = mem
                total_power += mem["power"]
                total_area += mem["area"]
                break

        # Connectivity
        for con in components["connectivity"]:
            if total_power + con["power"] <= max_power and total_area + con["area"] <= max_area:
                selected["connectivity"] = con
                total_power += con["power"]
                total_area += con["area"]
                break

        return render(request, "results.html", {
            "selection": selected,
            "power": total_power,
            "area": total_area
        })
    
    return render(request, "upload.html")
