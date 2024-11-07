import sys
from datetime import datetime, timedelta
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QPushButton, QLineEdit, QLabel, QMessageBox, QAction, QMenuBar, QSpinBox, QComboBox, QDateEdit, QTimeEdit, QTextEdit
from PyQt5.QtCore import QDate, QTime
from main import RecordatorioManager, HorarioManager, ActividadAcademicaManager, PlanEstudioManager, \
    CalificacionManager, MaterialManager, ProductividadManager, BalanceAcademicoManager, \
    MetaAcademicaManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor Académico")
        self.setGeometry(100, 100, 800, 600)

        self.recordatorio_manager = RecordatorioManager()
        self.horario_manager = HorarioManager()
        self.actividad_manager = ActividadAcademicaManager()
        self.plan_estudio_manager = PlanEstudioManager()
        self.calificacion_manager = CalificacionManager()
        self.material_manager = MaterialManager()
        self.productividad_manager = ProductividadManager()
        self.balance_manager = BalanceAcademicoManager()
        self.meta_manager = MetaAcademicaManager()

        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.crear_menu()

    def crear_menu(self):
        # Menú de actividades académicas
        menu_actividad = self.menu_bar.addMenu("Actividades")
        registrar_actividad_action = QAction("Registrar Actividad", self)
        registrar_actividad_action.triggered.connect(self.abrir_registrar_actividad)
        menu_actividad.addAction(registrar_actividad_action)

        ver_actividades_action = QAction("Ver Actividades", self)
        ver_actividades_action.triggered.connect(self.abrir_ver_actividades)
        menu_actividad.addAction(ver_actividades_action)

        # Menú de horarios
        menu_horario = self.menu_bar.addMenu("Horario")
        gestionar_horario_action = QAction("Gestionar Horario", self)
        gestionar_horario_action.triggered.connect(self.abrir_gestionar_horario)
        menu_horario.addAction(gestionar_horario_action)

        ver_horarios_action = QAction("Ver Horarios", self)
        ver_horarios_action.triggered.connect(self.abrir_ver_horarios)
        menu_horario.addAction(ver_horarios_action)

        # Menú de planificar estudio
        menu_plan_estudio = self.menu_bar.addMenu("Planificar Estudio")
        planificar_estudio_action = QAction("Planificar Estudio", self)
        planificar_estudio_action.triggered.connect(self.abrir_planificar_estudio)
        menu_plan_estudio.addAction(planificar_estudio_action)

        # Menú de ver planificaciones de estudio
        menu_ver_plan_estudio = self.menu_bar.addMenu("Ver Planificaciones")
        ver_plan_estudio_action = QAction("Ver Planificaciones de Estudio", self)
        ver_plan_estudio_action.triggered.connect(self.abrir_ver_planificaciones_estudio)
        menu_ver_plan_estudio.addAction(ver_plan_estudio_action)

        # Menú de calificaciones
        menu_calificaciones = self.menu_bar.addMenu("Calificaciones")
        registrar_calificacion_action = QAction("Registrar Calificación", self)
        registrar_calificacion_action.triggered.connect(self.abrir_registrar_calificacion)
        menu_calificaciones.addAction(registrar_calificacion_action)

        ver_calificaciones_action = QAction("Ver Calificaciones", self)
        ver_calificaciones_action.triggered.connect(self.abrir_ver_calificaciones)
        menu_calificaciones.addAction(ver_calificaciones_action)

        # Menú de recordatorios
        menu_recordatorio = self.menu_bar.addMenu("Recordatorios")
        configurar_recordatorio_action = QAction("Configurar Recordatorio", self)
        configurar_recordatorio_action.triggered.connect(self.abrir_configurar_recordatorio)
        menu_recordatorio.addAction(configurar_recordatorio_action)

        ver_recordatorios_action = QAction("Ver Recordatorios", self)
        ver_recordatorios_action.triggered.connect(self.abrir_ver_recordatorios)
        menu_recordatorio.addAction(ver_recordatorios_action)

        # Menú de material
        menu_material = self.menu_bar.addMenu("Material")
        organizar_material_action = QAction("Organizar Material", self)
        organizar_material_action.triggered.connect(self.abrir_organizar_material)
        menu_material.addAction(organizar_material_action)

        ver_material_action = QAction("Ver Material", self)
        ver_material_action.triggered.connect(self.abrir_ver_material)
        menu_material.addAction(ver_material_action)

        # Menú de productividad
        menu_productividad = self.menu_bar.addMenu("Productividad")
        registrar_tiempo_action = QAction("Registro de Tiempo", self)
        registrar_tiempo_action.triggered.connect(self.abrir_registrar_tiempo)
        menu_productividad.addAction(registrar_tiempo_action)

        ver_productividad_action = QAction("Ver Productividad", self)
        ver_productividad_action.triggered.connect(self.abrir_ver_productividad)
        menu_productividad.addAction(ver_productividad_action)

        menu_balance = self.menu_bar.addMenu("Balance Académico")

        controlar_balance_action = QAction("Controlar Balance Académico", self)
        controlar_balance_action.triggered.connect(self.abrir_controlar_balance)
        menu_balance.addAction(controlar_balance_action)

        ver_balance_action = QAction("Ver Balance", self)
        ver_balance_action.triggered.connect(self.abrir_ver_balance)
        menu_balance.addAction(ver_balance_action)

        menu_metas = self.menu_bar.addMenu("Metas")

        establecer_meta_action = QAction("Establecer Meta", self)
        establecer_meta_action.triggered.connect(self.abrir_establecer_meta)
        menu_metas.addAction(establecer_meta_action)

        ver_metas_action = QAction("Ver Metas", self)
        ver_metas_action.triggered.connect(self.abrir_ver_metas)
        menu_metas.addAction(ver_metas_action)

        menu_reportes = self.menu_bar.addMenu("Reportes")

        generar_reporte_action = QAction("Generar Reporte", self)
        generar_reporte_action.triggered.connect(self.abrir_generar_reporte)
        menu_reportes.addAction(generar_reporte_action)

        ver_reporte_action = QAction("Ver Reportes", self)
        ver_reporte_action.triggered.connect(self.abrir_ver_reportes)
        menu_reportes.addAction(ver_reporte_action)

    # Funcionalidades del menú
    def abrir_registrar_actividad(self):
        dialog = RegistrarActividadDialog(self.actividad_manager)
        dialog.exec_()

    def abrir_ver_actividades(self):
        dialog = VerActividadesDialog(self, self.actividad_manager)  # Pasa self como el parent
        dialog.exec_()

    def abrir_gestionar_horario(self):
        dialog = GestionarHorarioDialog(self.horario_manager)
        dialog.exec_()

    def abrir_ver_horarios(self):
        dialog = VerHorariosDialog(self.horario_manager)
        dialog.exec_()

    def abrir_planificar_estudio(self):
        dialog = PlanificarEstudioDialog(self.plan_estudio_manager)
        dialog.exec_()

    def abrir_ver_planificaciones_estudio(self):
        dialog = VerPlanificacionesEstudioDialog(self.plan_estudio_manager)
        dialog.exec_()

    def abrir_registrar_calificacion(self):
        dialog = RegistrarCalificacionDialog(self.calificacion_manager)
        dialog.exec_()

    def abrir_ver_calificaciones(self):
        dialog = VerCalificacionesDialog(self.calificacion_manager)
        dialog.exec_()

    def abrir_configurar_recordatorio(self):
        dialog = ConfigurarRecordatorioDialog(self.recordatorio_manager)
        dialog.exec_()

    def abrir_ver_recordatorios(self):
        dialog = VerRecordatoriosDialog(self.recordatorio_manager)
        dialog.exec_()

    def abrir_organizar_material(self):
        dialog = OrganizarMaterialDialog(self.material_manager)
        dialog.exec_()

    def abrir_ver_material(self):
        dialog = VerMaterialDialog(self.material_manager)
        dialog.exec_()

    def abrir_registrar_tiempo(self):
        dialog = RegistrarTiempoDialog(self.productividad_manager)
        dialog.exec_()

    def abrir_ver_productividad(self):
        dialog = VerProductividadDialog(self.productividad_manager)
        dialog.exec_()

    def abrir_controlar_balance(self):
        dialog = ControlarBalanceAcademicoDialog(self.balance_manager)
        dialog.exec_()

    def abrir_ver_balance(self):
        dialog = VerBalanceAcademicoDialog(self.balance_manager)
        dialog.exec_()

    def abrir_establecer_meta(self):
        dialog = EstablecerMetaDialog(self.meta_manager)
        dialog.exec_()

    def abrir_ver_metas(self):
        dialog = VerMetasDialog(self.meta_manager)
        dialog.exec_()

    def abrir_generar_reporte(self):
        dialog = GenerarReporteDialog(self.meta_manager)
        dialog.exec_()

    def abrir_ver_reportes(self):
        pass


class RegistrarActividadDialog(QDialog):
    def __init__(self, actividad_manager):
        super().__init__()
        self.setWindowTitle("Registrar Actividad")
        self.actividad_manager = actividad_manager

        layout = QVBoxLayout()

        self.tipo_input = QLineEdit()
        self.materia_input = QLineEdit()
        self.fecha_entrega_input = QLineEdit()
        self.descripcion_input = QLineEdit()

        # Añadir control de prioridad
        self.prioridad_input = QSpinBox(self)
        self.prioridad_input.setRange(1, 5)  # Limitar el rango de la prioridad a 1-5
        self.prioridad_input.setValue(1)  # Establecer un valor por defecto de 1

        layout.addWidget(QLabel("Tipo de Actividad"))
        layout.addWidget(self.tipo_input)

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Fecha de Entrega (dd/mm/yyyy)"))
        layout.addWidget(self.fecha_entrega_input)

        layout.addWidget(QLabel("Descripción"))
        layout.addWidget(self.descripcion_input)

        layout.addWidget(QLabel("Prioridad"))
        layout.addWidget(self.prioridad_input)  # Agregar el QSpinBox para la prioridad

        registrar_btn = QPushButton("Registrar")
        registrar_btn.clicked.connect(self.registrar_actividad)
        layout.addWidget(registrar_btn)

        self.setLayout(layout)

    def registrar_actividad(self):
        tipo = self.tipo_input.text()
        materia = self.materia_input.text()
        fecha_entrega = self.fecha_entrega_input.text()
        descripcion = self.descripcion_input.text()
        prioridad = self.prioridad_input.value()  # Obtener la prioridad seleccionada

        if tipo and materia and fecha_entrega and descripcion:
            # Registrar en la clase ActividadAcademicaManager
            try:
                mensaje = self.actividad_manager.registrar_actividad(tipo, materia, fecha_entrega, descripcion,
                                                                     prioridad)
                QMessageBox.information(self, "Éxito", mensaje)
            except ValueError as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")


# Diálogo para ver todas las actividades
class VerActividadesDialog(QDialog):
    def __init__(self, parent, actividad_manager):
        super().__init__(parent)
        self.setWindowTitle("Ver Actividades")
        self.actividad_manager = actividad_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Tipo", "Materia", "Fecha de Entrega", "Descripción", "Prioridad"])
        layout.addWidget(self.table)

        # Cargar actividades
        self.cargar_actividades()
        self.setLayout(layout)

    def cargar_actividades(self):
        try:
            actividades = self.actividad_manager.actividades
            if not actividades:
                raise ValueError("No hay actividades registradas.")
            self.table.setRowCount(len(actividades))

            for row, actividad in enumerate(actividades):
                tipo = actividad['tipo']
                materia = actividad['materia']
                fecha_entrega = actividad['fecha_entrega']
                descripcion = actividad['descripcion']
                prioridad = actividad['prioridad']

                # Convertir fecha_entrega a QDate si es un string
                if isinstance(fecha_entrega, str):
                    fecha_entrega = QDate.fromString(fecha_entrega, "dd/MM/yyyy")

                # Comprobar si la fecha es válida
                if not fecha_entrega.isValid():
                    raise ValueError(f"Fecha inválida para la actividad: {actividad}.")

                # Agregar datos a la tabla
                self.table.setItem(row, 0, QTableWidgetItem(tipo))
                self.table.setItem(row, 1, QTableWidgetItem(materia))
                self.table.setItem(row, 2, QTableWidgetItem(fecha_entrega.toString("dd/MM/yyyy")))
                self.table.setItem(row, 3, QTableWidgetItem(descripcion))
                self.table.setItem(row, 4, QTableWidgetItem(str(prioridad)))

        except Exception as e:
            print(f"Error en cargar actividades: {str(e)}")
            raise e  # Vuelve a lanzar el error para que lo capture el bloque try-except externo.


# Diálogo para gestionar horario
from PyQt5.QtWidgets import QColorDialog


# Diálogo para gestionar horario
class GestionarHorarioDialog(QDialog):
    def __init__(self, horario_manager):
        super().__init__()
        self.setWindowTitle("Gestionar Horario")
        self.horario_manager = horario_manager

        layout = QVBoxLayout()

        self.materia_input = QLineEdit()
        self.dia_input = QLineEdit()
        self.hora_inicio_input = QLineEdit()
        self.hora_fin_input = QLineEdit()

        # Campos para aula y color
        self.aula_input = QLineEdit()
        self.color_button = QPushButton("Seleccionar Color")
        self.color_button.clicked.connect(self.seleccionar_color)

        # Almacenar el color seleccionado
        self.color_asignado = None

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Día de la Semana"))
        layout.addWidget(self.dia_input)

        layout.addWidget(QLabel("Hora Inicio (HH:MM)"))
        layout.addWidget(self.hora_inicio_input)

        layout.addWidget(QLabel("Hora Fin (HH:MM)"))
        layout.addWidget(self.hora_fin_input)

        # Agregar los nuevos campos
        layout.addWidget(QLabel("Aula"))
        layout.addWidget(self.aula_input)

        layout.addWidget(self.color_button)

        agregar_btn = QPushButton("Agregar Clase")
        agregar_btn.clicked.connect(self.agregar_clase)
        layout.addWidget(agregar_btn)

        self.setLayout(layout)

    def seleccionar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_asignado = color.name()  # Guardar el color en formato hexadecimal
            self.color_button.setStyleSheet(f"background-color: {self.color_asignado};")

    def agregar_clase(self):
        materia = self.materia_input.text()
        dia = self.dia_input.text()
        hora_inicio_str = self.hora_inicio_input.text()
        hora_fin_str = self.hora_fin_input.text()
        aula = self.aula_input.text()

        if materia and dia and hora_inicio_str and hora_fin_str and aula and self.color_asignado:
            # Convertir las horas de inicio y fin a objetos QTime
            try:
                hora_inicio = QTime.fromString(hora_inicio_str, "HH:mm")
                hora_fin = QTime.fromString(hora_fin_str, "HH:mm")

                if not hora_inicio.isValid() or not hora_fin.isValid():
                    raise ValueError("Las horas de inicio o fin no son válidas.")

                mensaje = self.horario_manager.agregar_clase(
                    materia, dia, hora_inicio, hora_fin, aula, self.color_asignado)
                QMessageBox.information(self, "Éxito", mensaje)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al agregar clase: {str(e)}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")


# Diálogo para ver horarios
# Diálogo para ver horarios
class VerHorariosDialog(QDialog):
    def __init__(self, horario_manager):
        super().__init__()
        self.setWindowTitle("Ver Horarios")
        self.horario_manager = horario_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Ahora hay 4 columnas: Materia, Hora Inicio, Hora Fin, Color
        self.table.setHorizontalHeaderLabels(["Materia", "Hora Inicio", "Hora Fin", "Color"])
        layout.addWidget(self.table)

        # Cargar horarios
        self.cargar_horarios()
        self.setLayout(layout)

    def cargar_horarios(self):
        for dia, clases in self.horario_manager.horario.items():
            for clase in clases:
                row = self.table.rowCount()
                self.table.insertRow(row)

                # Insertar la materia
                self.table.setItem(row, 0, QTableWidgetItem(clase['materia']))

                # Convertir hora_inicio y hora_fin a cadenas con formato correcto
                hora_inicio = clase['hora_inicio']
                hora_fin = clase['hora_fin']

                if isinstance(hora_inicio, QTime):
                    hora_inicio_str = hora_inicio.toString("HH:mm")
                else:
                    hora_inicio_str = hora_inicio  # Asumir que es una cadena válida

                if isinstance(hora_fin, QTime):
                    hora_fin_str = hora_fin.toString("HH:mm")
                else:
                    hora_fin_str = hora_fin  # Asumir que es una cadena válida

                self.table.setItem(row, 1, QTableWidgetItem(hora_inicio_str))
                self.table.setItem(row, 2, QTableWidgetItem(hora_fin_str))

                # Mostrar el color asignado en la última columna
                color = clase['color']
                color_item = QTableWidgetItem("Color")
                color_item.setBackground(QColor(color))  # Establecer el fondo de la celda con el color
                self.table.setItem(row, 3, color_item)


class PlanificarEstudioDialog(QDialog):
    def __init__(self, plan_estudio_manager):
        super().__init__()
        self.setWindowTitle("Planificar Estudio")
        self.plan_estudio_manager = plan_estudio_manager

        layout = QVBoxLayout()

        self.materia_input = QLineEdit()
        self.tema_input = QLineEdit()
        self.duracion_input = QLineEdit()
        self.dificultad_input = QComboBox()

        self.dificultad_input.addItem("Baja")
        self.dificultad_input.addItem("Media")
        self.dificultad_input.addItem("Alta")

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Tema a Estudiar"))
        layout.addWidget(self.tema_input)

        layout.addWidget(QLabel("Duración Estimada (horas)"))
        layout.addWidget(self.duracion_input)

        layout.addWidget(QLabel("Nivel de Dificultad"))
        layout.addWidget(self.dificultad_input)

        planificar_btn = QPushButton("Planificar Estudio")
        planificar_btn.clicked.connect(self.planificar_estudio)
        layout.addWidget(planificar_btn)

        self.setLayout(layout)

    def planificar_estudio(self):
        materia = self.materia_input.text()
        tema = self.tema_input.text()
        duracion = self.duracion_input.text()
        dificultad = self.dificultad_input.currentText()

        if materia and tema and duracion and dificultad:
            try:
                duracion_float = float(duracion)
                if duracion_float <= 0:
                    raise ValueError("La duración debe ser un número positivo.")

                mensaje = self.plan_estudio_manager.planificar_estudio(materia, tema, duracion_float, dificultad)
                QMessageBox.information(self, "Éxito", mensaje)
            except ValueError as e:
                QMessageBox.critical(self, "Error", f"Error al planificar estudio: {str(e)}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")


# Diálogo para ver las planificaciones de estudio
class VerPlanificacionesEstudioDialog(QDialog):
    def __init__(self, plan_estudio_manager):
        super().__init__()
        self.setWindowTitle("Ver Planificaciones de Estudio")
        self.plan_estudio_manager = plan_estudio_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Materia", "Tema", "Duración", "Dificultad"])
        layout.addWidget(self.table)

        # Cargar planificaciones
        self.cargar_planificaciones()
        self.setLayout(layout)

    def cargar_planificaciones(self):
        planificaciones = self.plan_estudio_manager.planificaciones
        if not planificaciones:
            QMessageBox.warning(self, "No hay Planificaciones", "No hay planificaciones de estudio registradas.")
            return

        self.table.setRowCount(len(planificaciones))

        for row, plan in enumerate(planificaciones):
            self.table.setItem(row, 0, QTableWidgetItem(plan['materia']))
            self.table.setItem(row, 1, QTableWidgetItem(plan['tema']))
            self.table.setItem(row, 2, QTableWidgetItem(str(plan['duracion'])))
            self.table.setItem(row, 3, QTableWidgetItem(plan['dificultad']))


# Diálogo para registrar calificación
class RegistrarCalificacionDialog(QDialog):
    def __init__(self, calificacion_manager):
        super().__init__()
        self.setWindowTitle("Registrar Calificación")
        self.calificacion_manager = calificacion_manager

        layout = QVBoxLayout()

        self.materia_input = QLineEdit()
        self.tipo_input = QLineEdit()
        self.nota_input = QLineEdit()
        self.porcentaje_input = QLineEdit()

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Tipo de Evaluación"))
        layout.addWidget(self.tipo_input)

        layout.addWidget(QLabel("Nota Obtenida"))
        layout.addWidget(self.nota_input)

        layout.addWidget(QLabel("Porcentaje de la Nota (%)"))
        layout.addWidget(self.porcentaje_input)

        registrar_btn = QPushButton("Registrar Calificación")
        registrar_btn.clicked.connect(self.registrar_calificacion)
        layout.addWidget(registrar_btn)

        self.setLayout(layout)

    def registrar_calificacion(self):
        materia = self.materia_input.text()
        tipo = self.tipo_input.text()
        try:
            nota = float(self.nota_input.text())
            porcentaje = float(self.porcentaje_input.text())

            if not (0 <= nota <= 10):
                raise ValueError("La nota debe estar entre 0 y 10.")
            if not (0 <= porcentaje <= 100):
                raise ValueError("El porcentaje debe estar entre 0 y 100.")

            # Registrar calificación
            mensaje = self.calificacion_manager.registrar_calificacion(materia, tipo, nota, porcentaje)
            QMessageBox.information(self, "Éxito", mensaje)
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Error al registrar calificación: {str(e)}")


# Diálogo para ver calificaciones
class VerCalificacionesDialog(QDialog):
    def __init__(self, calificacion_manager):
        super().__init__()
        self.setWindowTitle("Ver Calificaciones")
        self.calificacion_manager = calificacion_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Materia", "Tipo de Evaluación", "Nota Obtenida", "Porcentaje", "Promedio"])
        layout.addWidget(self.table)

        # Cargar calificaciones
        self.cargar_calificaciones()
        self.setLayout(layout)

    def cargar_calificaciones(self):
        calificaciones = self.calificacion_manager.calificaciones
        if not calificaciones:
            QMessageBox.warning(self, "No hay Calificaciones", "No hay calificaciones registradas.")
            return

        self.table.setRowCount(len(calificaciones))

        for row, calificacion in enumerate(calificaciones):
            self.table.setItem(row, 0, QTableWidgetItem(calificacion['materia']))
            self.table.setItem(row, 1, QTableWidgetItem(calificacion['tipo']))
            self.table.setItem(row, 2, QTableWidgetItem(str(calificacion['nota'])))
            self.table.setItem(row, 3, QTableWidgetItem(str(calificacion['porcentaje'])))
            self.table.setItem(row, 4, QTableWidgetItem(str(calificacion['promedio'])))


# Diálogo para configurar recordatorio
class ConfigurarRecordatorioDialog(QDialog):
    def __init__(self, recordatorio_manager):
        super().__init__()
        self.setWindowTitle("Configurar Recordatorio")
        self.recordatorio_manager = recordatorio_manager

        layout = QVBoxLayout()

        # Tipo de recordatorio
        self.tipo_input = QLineEdit()
        layout.addWidget(QLabel("Tipo de Recordatorio"))
        layout.addWidget(self.tipo_input)

        # Fecha y hora del recordatorio
        self.fecha_input = QDateEdit()
        self.fecha_input.setDate(QDate.currentDate())
        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(self.fecha_input)

        self.hora_input = QTimeEdit()
        self.hora_input.setTime(QTime.currentTime())
        layout.addWidget(QLabel("Hora"))
        layout.addWidget(self.hora_input)

        # Frecuencia del recordatorio
        self.frecuencia_input = QComboBox()
        self.frecuencia_input.addItems(["Diaria", "Semanal", "Mensual"])
        layout.addWidget(QLabel("Frecuencia"))
        layout.addWidget(self.frecuencia_input)

        # Prioridad del recordatorio (1-5)
        self.prioridad_input = QComboBox()
        self.prioridad_input.addItems([str(i) for i in range(1, 6)])
        layout.addWidget(QLabel("Prioridad (1 a 5)"))
        layout.addWidget(self.prioridad_input)

        # Botón para configurar el recordatorio
        configurar_btn = QPushButton("Configurar Recordatorio")
        configurar_btn.clicked.connect(self.configurar_recordatorio)
        layout.addWidget(configurar_btn)

        self.setLayout(layout)

    def configurar_recordatorio(self):
        tipo = self.tipo_input.text()
        fecha = self.fecha_input.date().toString("dd/MM/yyyy")
        hora = self.hora_input.time().toString("HH:mm")
        frecuencia = self.frecuencia_input.currentText()
        prioridad = self.prioridad_input.currentText()

        fecha_hora = f"{fecha} {hora}"

        # Configurar el recordatorio
        mensaje = self.recordatorio_manager.configurar_recordatorio(tipo, fecha_hora, frecuencia, prioridad)
        QMessageBox.information(self, "Éxito", mensaje)


# Diálogo para ver los recordatorios
class VerRecordatoriosDialog(QDialog):
    def __init__(self, recordatorio_manager):
        super().__init__()
        self.setWindowTitle("Ver Recordatorios")
        self.recordatorio_manager = recordatorio_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Tipo", "Fecha y Hora", "Frecuencia", "Prioridad"])
        layout.addWidget(self.table)

        # Cargar recordatorios
        self.cargar_recordatorios()
        self.setLayout(layout)

    def cargar_recordatorios(self):
        recordatorios = self.recordatorio_manager.recordatorios
        if not recordatorios:
            QMessageBox.warning(self, "No hay Recordatorios", "No hay recordatorios programados.")
            return

        self.table.setRowCount(len(recordatorios))

        for row, recordatorio in enumerate(recordatorios):
            self.table.setItem(row, 0, QTableWidgetItem(recordatorio['tipo']))
            self.table.setItem(row, 1, QTableWidgetItem(recordatorio['fecha_hora']))
            self.table.setItem(row, 2, QTableWidgetItem(recordatorio['frecuencia']))
            self.table.setItem(row, 3, QTableWidgetItem(recordatorio['prioridad']))


# Diálogo para organizar material
class OrganizarMaterialDialog(QDialog):
    def __init__(self, material_manager):
        super().__init__()
        self.setWindowTitle("Organizar Material")
        self.material_manager = material_manager

        layout = QVBoxLayout()

        self.archivo_input = QLineEdit()
        self.materia_input = QLineEdit()
        self.tema_input = QLineEdit()
        self.etiquetas_input = QLineEdit()
        self.descripcion_input = QLineEdit()

        layout.addWidget(QLabel("Archivo"))
        layout.addWidget(self.archivo_input)

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Tema"))
        layout.addWidget(self.tema_input)

        layout.addWidget(QLabel("Etiquetas"))
        layout.addWidget(self.etiquetas_input)

        layout.addWidget(QLabel("Descripción"))
        layout.addWidget(self.descripcion_input)

        organizar_btn = QPushButton("Organizar Material")
        organizar_btn.clicked.connect(self.organizar_material)
        layout.addWidget(organizar_btn)

        self.setLayout(layout)

    def organizar_material(self):
        archivo = self.archivo_input.text()
        materia = self.materia_input.text()
        tema = self.tema_input.text()
        etiquetas = self.etiquetas_input.text().split(",")  # Separar las etiquetas por coma
        descripcion = self.descripcion_input.text()

        if archivo and materia and tema and etiquetas and descripcion:
            # Organizar el material
            material = self.material_manager.organizar_material(archivo, materia, tema, etiquetas, descripcion)
            QMessageBox.information(self, "Éxito", f"Material organizado: {material}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")


# Diálogo para ver material organizado
class VerMaterialDialog(QDialog):
    def __init__(self, material_manager):
        super().__init__()
        self.setWindowTitle("Ver Material")
        self.material_manager = material_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Archivo", "Materia", "Tema", "Etiquetas", "Descripción"])
        layout.addWidget(self.table)

        # Cargar los materiales organizados
        self.cargar_material()
        self.setLayout(layout)

    def cargar_material(self):
        materiales = self.material_manager.materiales
        if not materiales:
            QMessageBox.warning(self, "No hay Material", "No hay material organizado.")
            return

        self.table.setRowCount(len(materiales))

        for row, material in enumerate(materiales):
            self.table.setItem(row, 0, QTableWidgetItem(material['archivo']))
            self.table.setItem(row, 1, QTableWidgetItem(material['materia']))
            self.table.setItem(row, 2, QTableWidgetItem(material['tema']))
            self.table.setItem(row, 3, QTableWidgetItem(", ".join(material['etiquetas'])))
            self.table.setItem(row, 4, QTableWidgetItem(material['descripcion']))


class RegistrarTiempoDialog(QDialog):
    def __init__(self, productividad_manager):
        super().__init__()
        self.setWindowTitle("Registro de Tiempo de Estudio")
        self.productividad_manager = productividad_manager

        layout = QVBoxLayout()

        self.materia_input = QLineEdit()
        self.hora_inicio_input = QLineEdit()
        self.hora_fin_input = QLineEdit()
        self.concentracion_input = QLineEdit()

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Hora Inicio (HH:MM)"))
        layout.addWidget(self.hora_inicio_input)

        layout.addWidget(QLabel("Hora Fin (HH:MM)"))
        layout.addWidget(self.hora_fin_input)

        layout.addWidget(QLabel("Nivel de Concentración (1-5)"))
        layout.addWidget(self.concentracion_input)

        registrar_btn = QPushButton("Registrar Tiempo")
        registrar_btn.clicked.connect(self.registrar_tiempo)
        layout.addWidget(registrar_btn)

        self.setLayout(layout)

    def registrar_tiempo(self):
        materia = self.materia_input.text()
        hora_inicio_str = self.hora_inicio_input.text()
        hora_fin_str = self.hora_fin_input.text()
        concentracion_str = self.concentracion_input.text()

        if materia and hora_inicio_str and hora_fin_str and concentracion_str:
            try:
                # Convertir las horas de inicio y fin a objetos QTime
                hora_inicio = QTime.fromString(hora_inicio_str, "HH:mm")
                hora_fin = QTime.fromString(hora_fin_str, "HH:mm")
                concentracion = int(concentracion_str)

                if not hora_inicio.isValid() or not hora_fin.isValid() or concentracion < 1 or concentracion > 5:
                    raise ValueError("Datos de tiempo o concentración inválidos.")

                # Registrar el tiempo y calcular la productividad
                mensaje = self.productividad_manager.registrar_tiempo_estudio(materia, hora_inicio, hora_fin,
                                                                              concentracion)
                QMessageBox.information(self, "Éxito", mensaje)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al registrar tiempo: {str(e)}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")


# Diálogo para ver el registro de la productividad
class VerProductividadDialog(QDialog):
    def __init__(self, productividad_manager):
        super().__init__()
        self.setWindowTitle("Ver Productividad")
        self.productividad_manager = productividad_manager

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Materia", "Hora Inicio", "Hora Fin", "Nivel Concentración", "Productividad"])
        layout.addWidget(self.table)

        # Cargar registros de productividad
        self.cargar_productividad()
        self.setLayout(layout)

    def cargar_productividad(self):
        registros = self.productividad_manager.registros_productividad
        if not registros:
            QMessageBox.warning(self, "Sin registros", "No hay registros de productividad.")
            return

        self.table.setRowCount(len(registros))

        for row, registro in enumerate(registros):
            self.table.setItem(row, 0, QTableWidgetItem(registro['materia']))
            self.table.setItem(row, 1, QTableWidgetItem(registro['hora_inicio'].toString("HH:mm")))
            self.table.setItem(row, 2, QTableWidgetItem(registro['hora_fin'].toString("HH:mm")))
            self.table.setItem(row, 3, QTableWidgetItem(str(registro['concentracion'])))
            self.table.setItem(row, 4, QTableWidgetItem(f"{registro['productividad']}%"))


class ControlarBalanceAcademicoDialog(QDialog):
    def __init__(self, balance_manager):
        super().__init__()
        self.setWindowTitle("Controlar Balance Académico")
        self.balance_manager = balance_manager

        layout = QVBoxLayout()

        self.actividades_input = QLineEdit()
        self.descanso_input = QLineEdit()
        self.extracurriculares_input = QLineEdit()

        layout.addWidget(QLabel("Actividades Académicas Programadas (en horas)"))
        layout.addWidget(self.actividades_input)

        layout.addWidget(QLabel("Tiempo de Descanso (en horas)"))
        layout.addWidget(self.descanso_input)

        layout.addWidget(QLabel("Cantidad de Actividades Extracurriculares"))
        layout.addWidget(self.extracurriculares_input)

        registrar_btn = QPushButton("Registrar Actividad")
        registrar_btn.clicked.connect(self.registrar_balance)
        layout.addWidget(registrar_btn)

        self.setLayout(layout)

    def registrar_balance(self):
        try:
            actividades = float(self.actividades_input.text())
            descanso = float(self.descanso_input.text())
            extracurriculares = int(self.extracurriculares_input.text())

            # Registrar actividades académicas
            self.balance_manager.registrar_actividad_balance('Academica', actividades, datetime.now())
            # Registrar descanso
            self.balance_manager.registrar_actividad_balance('Descanso', descanso, datetime.now(), es_academica=False)
            # Registrar actividades extracurriculares
            self.balance_manager.registrar_actividad_balance('Extracurricular', extracurriculares, datetime.now(),
                                                             es_academica=False)

            QMessageBox.information(self, "Éxito", "Balance registrado correctamente.")
            self.close()
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese valores válidos.")


class VerBalanceAcademicoDialog(QDialog):
    def __init__(self, balance_manager):
        super().__init__()
        self.setWindowTitle("Ver Balance Académico")
        self.balance_manager = balance_manager

        layout = QVBoxLayout()
        self.texto_balance = QTextEdit()
        self.texto_balance.setReadOnly(True)
        layout.addWidget(self.texto_balance)

        # Cargar y analizar balance
        self.mostrar_balance()

        self.setLayout(layout)

    def mostrar_balance(self):
        fecha_actual = datetime.now()
        fecha_inicio = fecha_actual - timedelta(weeks=4)  # Analizar el balance de las últimas 4 semanas

        balance = self.balance_manager.analizar_balance(fecha_inicio, fecha_actual)
        alerta = self.balance_manager.verificar_sobrecarga()

        if alerta['alerta']:
            self.texto_balance.setText(f"¡Alerta! {alerta['mensaje']}\n\n")
        else:
            self.texto_balance.setText("Balance académico dentro de los límites recomendados.\n\n")

        self.texto_balance.append(f"Tiempo Académico: {balance['tiempo_academico']} horas")
        self.texto_balance.append(f"Tiempo de Descanso: {balance['tiempo_descanso']} horas")
        self.texto_balance.append(f"Porcentaje Académico: {balance['porcentaje_academico']:.2f}%")
        self.texto_balance.append(f"Porcentaje de Descanso: {balance['porcentaje_descanso']:.2f}%")
        self.texto_balance.append(f"Estado del Balance: {balance['estado_balance']}")


class EstablecerMetaDialog(QDialog):
    def __init__(self, meta_manager):
        super().__init__()
        self.setWindowTitle("Establecer Meta Académica")
        self.meta_manager = meta_manager

        layout = QVBoxLayout()

        self.objetivo_input = QLineEdit()
        self.materia_input = QLineEdit()
        self.fecha_limite_input = QDateEdit()
        self.fecha_limite_input.setDisplayFormat("dd/MM/yyyy")
        self.criterios_input = QTextEdit()

        layout.addWidget(QLabel("Objetivo"))
        layout.addWidget(self.objetivo_input)

        layout.addWidget(QLabel("Materia"))
        layout.addWidget(self.materia_input)

        layout.addWidget(QLabel("Fecha Límite"))
        layout.addWidget(self.fecha_limite_input)

        layout.addWidget(QLabel("Criterios de Cumplimiento"))
        layout.addWidget(self.criterios_input)

        establecer_btn = QPushButton("Establecer Meta")
        establecer_btn.clicked.connect(self.establecer_meta)
        layout.addWidget(establecer_btn)

        self.setLayout(layout)

    def establecer_meta(self):
        try:
            objetivo = self.objetivo_input.text()
            materia = self.materia_input.text()
            fecha_limite = self.fecha_limite_input.date().toPyDate()
            criterios = self.criterios_input.toPlainText()

            # Establecer meta
            self.meta_manager.establecer_meta(objetivo, materia, fecha_limite, criterios)

            QMessageBox.information(self, "Éxito", "Meta establecida correctamente.")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


class VerMetasDialog(QDialog):
    def __init__(self, meta_manager):
        super().__init__()
        self.setWindowTitle("Ver Metas Académicas")
        self.meta_manager = meta_manager

        layout = QVBoxLayout()
        self.lista_metas = QTextEdit()
        self.lista_metas.setReadOnly(True)
        layout.addWidget(self.lista_metas)

        # Mostrar metas activas
        self.mostrar_metas()

        self.setLayout(layout)

    def mostrar_metas(self):
        metas_activas = self.meta_manager.consultar_metas_activas()
        texto = ""
        for meta in metas_activas:
            texto += f"Objetivo: {meta['objetivo']}\n"
            texto += f"Materia: {meta['materia']}\n"
            texto += f"Fecha Límite: {meta['fecha_limite']}\n"
            texto += f"Progreso: {meta['progreso']}%\n"
            texto += f"Estado: {meta['estado']}\n"
            texto += f"Criterios: {meta['criterios']}\n\n"
        self.lista_metas.setText(texto)


class GenerarReporteDialog(QDialog):
    def __init__(self, meta_manager):
        super().__init__()
        self.setWindowTitle("Generar Reporte Académico")
        self.meta_manager = meta_manager

        layout = QVBoxLayout()

        self.fecha_inicio_input = QDateEdit()
        self.fecha_inicio_input.setDisplayFormat("dd/MM/yyyy")
        self.fecha_fin_input = QDateEdit()
        self.fecha_fin_input.setDisplayFormat("dd/MM/yyyy")
        self.materias_input = QLineEdit()  # Puede ingresar materias separadas por coma
        self.tipo_reporte_input = QComboBox()
        self.tipo_reporte_input.addItems(['completo', 'calificaciones', 'productividad', 'metas'])

        layout.addWidget(QLabel("Fecha de Inicio"))
        layout.addWidget(self.fecha_inicio_input)

        layout.addWidget(QLabel("Fecha de Fin"))
        layout.addWidget(self.fecha_fin_input)

        layout.addWidget(QLabel("Materias a Incluir (Separadas por coma)"))
        layout.addWidget(self.materias_input)

        layout.addWidget(QLabel("Tipo de Reporte"))
        layout.addWidget(self.tipo_reporte_input)

        generar_btn = QPushButton("Generar Reporte")
        generar_btn.clicked.connect(self.generar_reporte)
        layout.addWidget(generar_btn)

        self.setLayout(layout)

    def generar_reporte(self):
        try:
            periodo_inicio = self.fecha_inicio_input.date().toPyDate()
            periodo_fin = self.fecha_fin_input.date().toPyDate()
            materias = self.materias_input.text().split(",") if self.materias_input.text() else None
            tipo_reporte = self.tipo_reporte_input.currentText()

            # Generar el reporte
            reporte = self.meta_manager.generar_reporte(periodo_inicio, periodo_fin, materias, tipo_reporte)

            # Mostrar el reporte en otro cuadro
            self.mostrar_reporte(reporte)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def mostrar_reporte(self, reporte):
        reporte_texto = f"Reporte Generado: {reporte['tipo_reporte']}\n\n"
        reporte_texto += f"Periodo: {reporte['periodo']['inicio']} - {reporte['periodo']['fin']}\n"
        reporte_texto += f"Materias Analizadas: {', '.join(reporte['materias_analizadas'])}\n"
        reporte_texto += f"Fecha de Generación: {reporte['fecha_generacion']}\n\n"

        # Añadir análisis
        if 'analisis_calificaciones' in reporte:
            reporte_texto += "\nAnálisis de Calificaciones:\n"
            # Aquí agregamos las estadísticas de calificaciones, por ejemplo:
            reporte_texto += str(reporte['analisis_calificaciones'])

        if 'analisis_productividad' in reporte:
            reporte_texto += "\nAnálisis de Productividad:\n"
            reporte_texto += str(reporte['analisis_productividad'])

        if 'analisis_metas' in reporte:
            reporte_texto += "\nAnálisis de Cumplimiento de Metas:\n"
            reporte_texto += str(reporte['analisis_metas'])

        # Recomendaciones
        if 'recomendaciones' in reporte:
            reporte_texto += "\nRecomendaciones:\n"
            reporte_texto += "\n".join(reporte['recomendaciones'])

        # Mostrar en un cuadro de texto
        self.reporte_texto = QTextEdit()
        self.reporte_texto.setReadOnly(True)
        self.reporte_texto.setText(reporte_texto)

        layout = QVBoxLayout()
        layout.addWidget(self.reporte_texto)
        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
