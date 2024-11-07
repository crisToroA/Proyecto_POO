from datetime import datetime, timedelta


# Clases de Gestión
class RecordatorioManager:
    def __init__(self):
        self.recordatorios = []  # Lista para almacenar los recordatorios

    def configurar_recordatorio(self, tipo, fecha_hora, frecuencia, prioridad):
        # Añadir un nuevo recordatorio
        self.recordatorios.append({
            "tipo": tipo,
            "fecha_hora": fecha_hora,
            "frecuencia": frecuencia,
            "prioridad": prioridad
        })
        return f"Recordatorio programado: {tipo} para el {fecha_hora}."


class HorarioManager:
    def __init__(self):
        self.horario = {}

    def agregar_clase(self, materia, dia, hora_inicio, hora_fin, aula, color):
        # Almacenar la clase con todos los datos
        if dia not in self.horario:
            self.horario[dia] = []

        clase = {
            'materia': materia,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'aula': aula,
            'color': color
        }
        self.horario[dia].append(clase)
        return f"Clase de {materia} agregada el {dia} de {hora_inicio.toString('HH:mm')} a {hora_fin.toString('HH:mm')} en el aula {aula} con color {color}."


class ActividadAcademicaManager:
    def __init__(self):
        self.actividades = []

    def registrar_actividad(self, tipo, materia, fecha_entrega, descripcion, prioridad):
        nueva_actividad = {
            'tipo': tipo,
            'materia': materia,
            'fecha_entrega': fecha_entrega,
            'descripcion': descripcion,
            'prioridad': prioridad,
            'estado': 'Pendiente'
        }

        self.actividades.append(nueva_actividad)
        self.actividades.sort(key=lambda x: x['fecha_entrega'])
        return "Actividad registrada exitosamente"

    def modificar_actividad(self, tipo, materia, fecha_entrega, nueva_descripcion, nueva_prioridad):
        for actividad in self.actividades:
            if (actividad['tipo'] == tipo and
                    actividad['materia'] == materia and
                    actividad['fecha_entrega'] == fecha_entrega):
                actividad['descripcion'] = nueva_descripcion
                actividad['prioridad'] = nueva_prioridad
                return "Actividad modificada exitosamente"
        return "Actividad no encontrada"


class PlanEstudioManager:
    def __init__(self):
        self.planificaciones = []  # Almacenamos las planificaciones

    def planificar_estudio(self, materia, tema, duracion, dificultad):
        # Añadir una nueva planificación a la lista
        self.planificaciones.append({
            "materia": materia,
            "tema": tema,
            "duracion": duracion,
            "dificultad": dificultad
        })
        return "Estudio planificado exitosamente."


class CalificacionManager:
    def __init__(self):
        self.calificaciones = []  # Almacenamos las calificaciones

    def registrar_calificacion(self, materia, tipo, nota, porcentaje):
        # Añadir una nueva calificación
        self.calificaciones.append({
            "materia": materia,
            "tipo": tipo,
            "nota": nota,
            "porcentaje": porcentaje,
            "promedio": self.calcular_promedio(nota, porcentaje)
        })
        return f"Calificación registrada para {materia} - {tipo}."

    def calcular_promedio(self, nueva_nota, porcentaje):
        # Cálculo del promedio actualizado
        total_nota = sum([calificacion['nota'] * (calificacion['porcentaje'] / 100)
                          for calificacion in self.calificaciones])
        total_porcentaje = sum([calificacion['porcentaje'] for calificacion in self.calificaciones])

        if total_porcentaje == 0:
            return nueva_nota * (porcentaje / 100)  # Si no hay calificaciones, retorna la nueva calificación.
        return total_nota / total_porcentaje * 100  # Promedio ponderado.


class MaterialManager:
    def __init__(self):
        self.materiales = []  # Lista de materiales organizados

    def organizar_material(self, archivo, materia, tema, etiquetas, descripcion):
        # Crear un nuevo material organizado
        material = {
            'archivo': archivo,
            'materia': materia,
            'tema': tema,
            'etiquetas': etiquetas,
            'descripcion': descripcion
        }
        self.materiales.append(material)
        return f"Material '{archivo}' organizado con éxito."


class ProductividadManager:
    def __init__(self):
        self.registros_productividad = []  # Lista de registros de tiempo y productividad

    def registrar_tiempo_estudio(self, materia, hora_inicio, hora_fin, concentracion):
        # Calcular la duración del estudio en minutos
        duracion = hora_inicio.secsTo(hora_fin) / 60  # Duración en minutos

        # Análisis de productividad (de acuerdo con el nivel de concentración)
        productividad = self.calcular_productividad(duracion, concentracion)

        # Crear un nuevo registro de productividad
        registro = {
            'materia': materia,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'concentracion': concentracion,
            'productividad': productividad
        }

        self.registros_productividad.append(registro)
        return f"Tiempo de estudio registrado para {materia}. Productividad: {productividad}%"

    def calcular_productividad(self, duracion, concentracion):
        # Un simple análisis de productividad: la productividad mejora según el nivel de concentración
        if concentracion == 1:
            return min(100, duracion * 2)  # Alta productividad
        elif concentracion == 5:
            return max(40, duracion * 0.8)  # Baja productividad
        else:
            return min(80, duracion * (1.5 - concentracion * 0.2))  # Productividad moderada


class BalanceAcademicoManager:
    def __init__(self):
        self.balance_actividades = []

    def registrar_actividad_balance(self, tipo, duracion, fecha, es_academica=True):
        actividad = {
            'tipo': tipo,
            'duracion': duracion,
            'fecha': fecha,
            'es_academica': es_academica
        }

        self.balance_actividades.append(actividad)
        return "Actividad registrada en balance"

    def analizar_balance(self, fecha_inicio, fecha_fin):
        actividades_periodo = [
            act for act in self.balance_actividades
            if fecha_inicio <= act['fecha'] <= fecha_fin
        ]

        tiempo_academico = sum(
            act['duracion']
            for act in actividades_periodo
            if act['es_academica']
        )

        tiempo_descanso = sum(
            act['duracion']
            for act in actividades_periodo
            if not act['es_academica']
        )

        total_horas = tiempo_academico + tiempo_descanso

        analisis = {
            'tiempo_academico': tiempo_academico,
            'tiempo_descanso': tiempo_descanso,
            'porcentaje_academico': (tiempo_academico / total_horas * 100) if total_horas > 0 else 0,
            'porcentaje_descanso': (tiempo_descanso / total_horas * 100) if total_horas > 0 else 0,
            'estado_balance': self._evaluar_balance(tiempo_academico, tiempo_descanso)
        }

        return analisis

    def _evaluar_balance(self, tiempo_academico, tiempo_descanso):
        ratio_recomendado = 0.7

        if tiempo_academico + tiempo_descanso == 0:
            return "Sin datos suficientes"

        ratio_actual = tiempo_academico / (tiempo_academico + tiempo_descanso)

        if ratio_actual > ratio_recomendado + 0.1:
            return "Sobrecarga académica"
        elif ratio_actual < ratio_recomendado - 0.1:
            return "Exceso de tiempo libre"
        else:
            return "Balance adecuado"

    def verificar_sobrecarga(self):
        fecha_actual = datetime.now()
        fecha_inicio = fecha_actual - timedelta(days=7)

        balance = self.analizar_balance(fecha_inicio, fecha_actual)

        if balance['estado_balance'] == "Sobrecarga académica":
            return {
                'alerta': True,
                'mensaje': "Detectada sobrecarga académica. Se recomienda aumentar tiempo de descanso.",
                'datos': balance
            }
        return {'alerta': False}


class MetaAcademicaManager:
    def __init__(self):
        self.metas_academicas = []
        self.historial_logros = []

    def establecer_meta(self, objetivo, materia, fecha_limite, criterios):
        meta = {
            'objetivo': objetivo,
            'materia': materia,
            'fecha_limite': fecha_limite,
            'criterios': criterios,
            'estado': 'En progreso',
            'progreso': 0,
            'fecha_creacion': datetime.now()
        }

        self.metas_academicas.append(meta)
        return "Meta académica establecida exitosamente"

    def actualizar_progreso_meta(self, objetivo, materia, nuevo_progreso):
        for meta in self.metas_academicas:
            if meta['objetivo'] == objetivo and meta['materia'] == materia:
                meta['progreso'] = nuevo_progreso
                if nuevo_progreso >= 100:
                    meta['estado'] = 'Completada'
                    self._registrar_logro(meta)
                return "Progreso de meta actualizado"
        return "Meta no encontrada"

    def _registrar_logro(self, meta):
        logro = {
            'meta': meta['objetivo'],
            'materia': meta['materia'],
            'fecha_logro': datetime.now(),
            'tiempo_completado': (datetime.now() - meta['fecha_creacion']).days
        }
        self.historial_logros.append(logro)

    def consultar_metas_activas(self):
        return [meta for meta in self.metas_academicas if meta['estado'] == 'En progreso']

    def generar_reporte(self, periodo_inicio, periodo_fin, materias=None, tipo_reporte='completo'):
        reporte = {
            'periodo': {
                'inicio': periodo_inicio,
                'fin': periodo_fin
            },
            'materias_analizadas': materias if materias else 'Todas',
            'tipo_reporte': tipo_reporte,
            'fecha_generacion': datetime.now()
        }

        if tipo_reporte in ['completo', 'calificaciones']:
            reporte['analisis_calificaciones'] = self._analizar_calificaciones(
                periodo_inicio, periodo_fin, materias
            )

        if tipo_reporte in ['completo', 'productividad']:
            reporte['analisis_productividad'] = self._analizar_productividad_periodo(
                periodo_inicio, periodo_fin, materias
            )

        if tipo_reporte in ['completo', 'metas']:
            reporte['analisis_metas'] = self._analizar_cumplimiento_metas(
                periodo_inicio, periodo_fin, materias
            )

        reporte['recomendaciones'] = self._generar_recomendaciones(reporte)

        return reporte

    def _analizar_calificaciones(self, inicio, fin, materias=None):
        return {
            'promedios_por_materia': {},
            'tendencia': 'ascendente',
            'materias_criticas': []
        }

    def _analizar_productividad_periodo(self, inicio, fin, materias=None):
        return {
            'horas_estudio_total': 0,
            'eficiencia_promedio': 0,
            'distribucion_tiempo': {}
        }

    def _analizar_cumplimiento_metas(self, inicio, fin, materias=None):
        return {
            'metas_completadas': 0,
            'metas_pendientes': 0,
            'tasa_cumplimiento': 0
        }

    def _generar_recomendaciones(self, datos_reporte):
        recomendaciones = []

        if 'analisis_calificaciones' in datos_reporte:
            for materia in datos_reporte['analisis_calificaciones'].get('materias_criticas', []):
                recomendaciones.append(f"Aumentar horas de estudio en {materia}")

        if 'analisis_productividad' in datos_reporte:
            if datos_reporte['analisis_productividad']['eficiencia_promedio'] < 0.7:
                recomendaciones.append("Implementar técnicas de estudio más efectivas")

        return recomendaciones
