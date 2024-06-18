from django.db import models
from desafioadl.models import Tarea, Subtarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    #tareas = Tarea.objects.exclude(eliminada=True) hace lo mismo que arriba solo que excluye si eliminado es verdadero
    filtro = []
    for tarea in tareas:
        subtareas = Subtarea.objects.filter(tarea_id=tarea, eliminada=False)
        filtro.append({
            'tarea': tarea,
            'subtareas': list(subtareas)
        })
    return filtro


def crear_nueva_tarea(descripcion=''):
    Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def crear_sub_tarea(tarea_id, descripcion=''):
    tarea = Tarea.objects.get(id=tarea_id)
    Subtarea.objects.create(tarea_id=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()


def elimina_sub_tarea(subtarea_id):
    subtarea = Subtarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea_info in tareas_y_subtareas:
        tarea = tarea_info['tarea']
        subtareas = tarea_info['subtareas']
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f"...... [{subtarea.id}] {subtarea.descripcion}")
