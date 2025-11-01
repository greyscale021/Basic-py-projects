import psutil


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    cores = psutil.cpu_count(logical=True)
    return {"cpu": cpu_percent, "cores": cores}

def get_memory_usage():
    virtual_memory = psutil.virtual_memory()
    return {
        "used": virtual_memory.used,
        "total": virtual_memory.total,
        "percent": virtual_memory.percent
    }

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
