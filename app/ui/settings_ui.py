# Form implementation generated from reading ui file '/Users/immmax/development/_projects/DevTeam/BrainRing/app/ui/settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsForm(object):
    def setupUi(self, SettingsForm):
        SettingsForm.setObjectName("SettingsForm")
        SettingsForm.resize(782, 519)
        SettingsForm.setMinimumSize(QtCore.QSize(782, 519))
        SettingsForm.setMaximumSize(QtCore.QSize(782, 519))
        SettingsForm.setAutoFillBackground(False)
        self.frame = QtWidgets.QFrame(parent=SettingsForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 741, 441))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTimer = QtWidgets.QWidget()
        self.tabTimer.setAutoFillBackground(False)
        self.tabTimer.setObjectName("tabTimer")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tabTimer)
        self.layoutWidget.setGeometry(QtCore.QRect(51, 41, 423, 230))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_round_duration = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_round_duration.setFont(font)
        self.label_round_duration.setObjectName("label_round_duration")
        self.horizontalLayout_4.addWidget(self.label_round_duration)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.spinBox_round_duration = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBox_round_duration.setMinimum(20)
        self.spinBox_round_duration.setMaximum(300)
        self.spinBox_round_duration.setSingleStep(5)
        self.spinBox_round_duration.setProperty("value", 60)
        self.spinBox_round_duration.setObjectName("spinBox_round_duration")
        self.horizontalLayout_4.addWidget(self.spinBox_round_duration)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_time_after_wrong_answer = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_time_after_wrong_answer.setFont(font)
        self.label_time_after_wrong_answer.setObjectName("label_time_after_wrong_answer")
        self.verticalLayout_12.addWidget(self.label_time_after_wrong_answer)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_7.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_remaining_time = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.radioButton_remaining_time.setChecked(True)
        self.radioButton_remaining_time.setObjectName("radioButton_remaining_time")
        self.verticalLayout_6.addWidget(self.radioButton_remaining_time)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_fixed_time = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.radioButton_fixed_time.setChecked(False)
        self.radioButton_fixed_time.setObjectName("radioButton_fixed_time")
        self.horizontalLayout_5.addWidget(self.radioButton_fixed_time)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.spinBox_fixed_time_amount = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBox_fixed_time_amount.setMinimum(10)
        self.spinBox_fixed_time_amount.setMaximum(30)
        self.spinBox_fixed_time_amount.setSingleStep(5)
        self.spinBox_fixed_time_amount.setProperty("value", 20)
        self.spinBox_fixed_time_amount.setObjectName("spinBox_fixed_time_amount")
        self.horizontalLayout_5.addWidget(self.spinBox_fixed_time_amount)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        self.gridLayout.addLayout(self.verticalLayout_12, 2, 0, 1, 1)
        self.checkBox_timer_louder_sound_when_round_time_runs_out = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.checkBox_timer_louder_sound_when_round_time_runs_out.setFont(font)
        self.checkBox_timer_louder_sound_when_round_time_runs_out.setChecked(True)
        self.checkBox_timer_louder_sound_when_round_time_runs_out.setTristate(False)
        self.checkBox_timer_louder_sound_when_round_time_runs_out.setObjectName("checkBox_timer_louder_sound_when_round_time_runs_out")
        self.gridLayout.addWidget(self.checkBox_timer_louder_sound_when_round_time_runs_out, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tabTimer, "")
        self.tabScore = QtWidgets.QWidget()
        self.tabScore.setObjectName("tabScore")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.tabScore)
        self.layoutWidget1.setGeometry(QtCore.QRect(380, 260, 321, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.radioButton_endgane_notauto = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_endgane_notauto.setObjectName("radioButton_endgane_notauto")
        self.gridLayout_8.addWidget(self.radioButton_endgane_notauto, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_endgame_Nanswer = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_endgame_Nanswer.setChecked(True)
        self.radioButton_endgame_Nanswer.setObjectName("radioButton_endgame_Nanswer")
        self.horizontalLayout_3.addWidget(self.radioButton_endgame_Nanswer)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.spinBox_endgame_Nanswer = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.spinBox_endgame_Nanswer.setMinimum(1)
        self.spinBox_endgame_Nanswer.setMaximum(25)
        self.spinBox_endgame_Nanswer.setObjectName("spinBox_endgame_Nanswer")
        self.horizontalLayout_3.addWidget(self.spinBox_endgame_Nanswer)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_endgame_Nscore = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_endgame_Nscore.setObjectName("radioButton_endgame_Nscore")
        self.horizontalLayout_2.addWidget(self.radioButton_endgame_Nscore)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.spinBox_endgame_Nscore = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.spinBox_endgame_Nscore.setObjectName("spinBox_endgame_Nscore")
        self.horizontalLayout_2.addWidget(self.spinBox_endgame_Nscore)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.label_end_game = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_end_game.setFont(font)
        self.label_end_game.setObjectName("label_end_game")
        self.gridLayout_8.addWidget(self.label_end_game, 1, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.tabScore)
        self.layoutWidget2.setGeometry(QtCore.QRect(381, 41, 321, 102))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cost_question_group = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_cost_question_group.setMaximumSize(QtCore.QSize(9999999, 9999999))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_cost_question_group.setFont(font)
        self.label_cost_question_group.setObjectName("label_cost_question_group")
        self.verticalLayout_2.addWidget(self.label_cost_question_group)
        self.radioButton_always_one = QtWidgets.QRadioButton(parent=self.layoutWidget2)
        self.radioButton_always_one.setChecked(True)
        self.radioButton_always_one.setObjectName("radioButton_always_one")
        self.verticalLayout_2.addWidget(self.radioButton_always_one)
        self.radioButton_store_price = QtWidgets.QRadioButton(parent=self.layoutWidget2)
        self.radioButton_store_price.setObjectName("radioButton_store_price")
        self.verticalLayout_2.addWidget(self.radioButton_store_price)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_add_cost_answer = QtWidgets.QRadioButton(parent=self.layoutWidget2)
        self.radioButton_add_cost_answer.setObjectName("radioButton_add_cost_answer")
        self.horizontalLayout_7.addWidget(self.radioButton_add_cost_answer)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.spinBox_addcost_answer = QtWidgets.QSpinBox(parent=self.layoutWidget2)
        self.spinBox_addcost_answer.setObjectName("spinBox_addcost_answer")
        self.horizontalLayout_7.addWidget(self.spinBox_addcost_answer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.tabScore)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 260, 321, 72))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_two_answers = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_two_answers.setMaximumSize(QtCore.QSize(9999999, 99999))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(13)
        font.setBold(True)
        self.label_two_answers.setFont(font)
        self.label_two_answers.setObjectName("label_two_answers")
        self.verticalLayout.addWidget(self.label_two_answers)
        self.radioButton_draw_choice = QtWidgets.QRadioButton(parent=self.layoutWidget3)
        self.radioButton_draw_choice.setChecked(True)
        self.radioButton_draw_choice.setObjectName("radioButton_draw_choice")
        self.verticalLayout.addWidget(self.radioButton_draw_choice)
        self.radioButton_draw_auto = QtWidgets.QRadioButton(parent=self.layoutWidget3)
        self.radioButton_draw_auto.setObjectName("radioButton_draw_auto")
        self.verticalLayout.addWidget(self.radioButton_draw_auto)
        self.layoutWidget4 = QtWidgets.QWidget(parent=self.tabScore)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 40, 321, 133))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_score_group_2 = QtWidgets.QLabel(parent=self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_score_group_2.setFont(font)
        self.label_score_group_2.setObjectName("label_score_group_2")
        self.verticalLayout_22.addWidget(self.label_score_group_2)
        self.radioButton_score_auto_2 = QtWidgets.QRadioButton(parent=self.layoutWidget4)
        self.radioButton_score_auto_2.setChecked(True)
        self.radioButton_score_auto_2.setObjectName("radioButton_score_auto_2")
        self.verticalLayout_22.addWidget(self.radioButton_score_auto_2)
        self.radioButton_score_not_2 = QtWidgets.QRadioButton(parent=self.layoutWidget4)
        self.radioButton_score_not_2.setObjectName("radioButton_score_not_2")
        self.verticalLayout_22.addWidget(self.radioButton_score_not_2)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem13 = QtWidgets.QSpacerItem(28, 19, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_15.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(28, 19, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_15.addItem(spacerItem14)
        self.horizontalLayout_15.addLayout(self.verticalLayout_15)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.checkBox_score_fine_2 = QtWidgets.QCheckBox(parent=self.layoutWidget4)
        self.checkBox_score_fine_2.setObjectName("checkBox_score_fine_2")
        self.verticalLayout_13.addWidget(self.checkBox_score_fine_2)
        self.checkBox_score_clear_2 = QtWidgets.QCheckBox(parent=self.layoutWidget4)
        self.checkBox_score_clear_2.setObjectName("checkBox_score_clear_2")
        self.verticalLayout_13.addWidget(self.checkBox_score_clear_2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem15 = QtWidgets.QSpacerItem(28, 19, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_14.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(28, 19, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_14.addItem(spacerItem16)
        self.horizontalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_22.addLayout(self.horizontalLayout_15)
        self.tabWidget.addTab(self.tabScore, "")
        self.tabFalsestart = QtWidgets.QWidget()
        self.tabFalsestart.setObjectName("tabFalsestart")
        self.layoutWidget5 = QtWidgets.QWidget(parent=self.tabFalsestart)
        self.layoutWidget5.setGeometry(QtCore.QRect(50, 41, 514, 268))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_falsestart_off = QtWidgets.QRadioButton(parent=self.layoutWidget5)
        self.radioButton_falsestart_off.setChecked(True)
        self.radioButton_falsestart_off.setObjectName("radioButton_falsestart_off")
        self.verticalLayout_10.addWidget(self.radioButton_falsestart_off)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem17)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButton_falsestart_equal_wrong_answer = QtWidgets.QRadioButton(parent=self.layoutWidget5)
        self.radioButton_falsestart_equal_wrong_answer.setObjectName("radioButton_falsestart_equal_wrong_answer")
        self.verticalLayout_8.addWidget(self.radioButton_falsestart_equal_wrong_answer)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem19)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_falsestart_ignore_time_button = QtWidgets.QCheckBox(parent=self.layoutWidget5)
        self.checkBox_falsestart_ignore_time_button.setObjectName("checkBox_falsestart_ignore_time_button")
        self.horizontalLayout_8.addWidget(self.checkBox_falsestart_ignore_time_button)
        self.spinBox_duration_ignore_time_button = QtWidgets.QSpinBox(parent=self.layoutWidget5)
        self.spinBox_duration_ignore_time_button.setMinimum(3)
        self.spinBox_duration_ignore_time_button.setMaximum(15)
        self.spinBox_duration_ignore_time_button.setProperty("value", 5)
        self.spinBox_duration_ignore_time_button.setObjectName("spinBox_duration_ignore_time_button")
        self.horizontalLayout_8.addWidget(self.spinBox_duration_ignore_time_button)
        self.label_false_seconds = QtWidgets.QLabel(parent=self.layoutWidget5)
        self.label_false_seconds.setObjectName("label_false_seconds")
        self.horizontalLayout_8.addWidget(self.label_false_seconds)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem20)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_ignore_last_team_falsestart = QtWidgets.QCheckBox(parent=self.layoutWidget5)
        self.checkBox_ignore_last_team_falsestart.setObjectName("checkBox_ignore_last_team_falsestart")
        self.horizontalLayout_10.addWidget(self.checkBox_ignore_last_team_falsestart)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem21)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem22)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.radioButton_falsestart_block_team_button = QtWidgets.QRadioButton(parent=self.layoutWidget5)
        self.radioButton_falsestart_block_team_button.setObjectName("radioButton_falsestart_block_team_button")
        self.verticalLayout_9.addWidget(self.radioButton_falsestart_block_team_button)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_11.addItem(spacerItem23)
        self.horizontalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_falsestart_block_team_button = QtWidgets.QCheckBox(parent=self.layoutWidget5)
        self.checkBox_falsestart_block_team_button.setObjectName("checkBox_falsestart_block_team_button")
        self.horizontalLayout_6.addWidget(self.checkBox_falsestart_block_team_button)
        self.spinBox_falsestart_duration_block_team_button = QtWidgets.QSpinBox(parent=self.layoutWidget5)
        self.spinBox_falsestart_duration_block_team_button.setMinimum(5)
        self.spinBox_falsestart_duration_block_team_button.setMaximum(30)
        self.spinBox_falsestart_duration_block_team_button.setObjectName("spinBox_falsestart_duration_block_team_button")
        self.horizontalLayout_6.addWidget(self.spinBox_falsestart_duration_block_team_button)
        self.label_false_block_seconds = QtWidgets.QLabel(parent=self.layoutWidget5)
        self.label_false_block_seconds.setObjectName("label_false_block_seconds")
        self.horizontalLayout_6.addWidget(self.label_false_block_seconds)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem25)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem26)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tabFalsestart, "")
        self.tabProtocol = QtWidgets.QWidget()
        self.tabProtocol.setObjectName("tabProtocol")
        self.layoutWidget6 = QtWidgets.QWidget(parent=self.tabProtocol)
        self.layoutWidget6.setGeometry(QtCore.QRect(50, 40, 160, 49))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_keep_game_protocol = QtWidgets.QCheckBox(parent=self.layoutWidget6)
        self.checkBox_keep_game_protocol.setChecked(True)
        self.checkBox_keep_game_protocol.setObjectName("checkBox_keep_game_protocol")
        self.verticalLayout_4.addWidget(self.checkBox_keep_game_protocol)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem27)
        self.tabWidget.addTab(self.tabProtocol, "")
        self.layoutWidget7 = QtWidgets.QWidget(parent=SettingsForm)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 470, 761, 41))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_default = QtWidgets.QPushButton(parent=self.layoutWidget7)
        self.pushButton_default.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_default.setObjectName("pushButton_default")
        self.horizontalLayout_14.addWidget(self.pushButton_default)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.layoutWidget7)
        self.pushButton_save.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_14.addWidget(self.pushButton_save)
        self.pushButton_download = QtWidgets.QPushButton(parent=self.layoutWidget7)
        self.pushButton_download.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_14.addWidget(self.pushButton_download)
        self.pushButton_apply = QtWidgets.QPushButton(parent=self.layoutWidget7)
        self.pushButton_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_14.addWidget(self.pushButton_apply)
        self.pushButton_cansel = QtWidgets.QPushButton(parent=self.layoutWidget7)
        self.pushButton_cansel.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_cansel.setObjectName("pushButton_cansel")
        self.horizontalLayout_14.addWidget(self.pushButton_cansel)

        self.retranslateUi(SettingsForm)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SettingsForm)

    def retranslateUi(self, SettingsForm):
        _translate = QtCore.QCoreApplication.translate
        SettingsForm.setWindowTitle(_translate("SettingsForm", "Brain Ring - Настройки"))
        self.label_round_duration.setText(_translate("SettingsForm", "Время ответа на вопрос"))
        self.label.setText(_translate("SettingsForm", "сек"))
        self.label_time_after_wrong_answer.setText(_translate("SettingsForm", " После неверного ответа даётся:"))
        self.radioButton_remaining_time.setText(_translate("SettingsForm", "Оставшееся время"))
        self.radioButton_fixed_time.setText(_translate("SettingsForm", "Фиксированное время"))
        self.label_2.setText(_translate("SettingsForm", "сек"))
        self.checkBox_timer_louder_sound_when_round_time_runs_out.setText(_translate("SettingsForm", "Усиление звука таймера в последние 10 секунд"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTimer), _translate("SettingsForm", "Таймер"))
        self.radioButton_endgane_notauto.setText(_translate("SettingsForm", "Не завершается автоматически"))
        self.radioButton_endgame_Nanswer.setText(_translate("SettingsForm", "До количества вопросов"))
        self.radioButton_endgame_Nscore.setText(_translate("SettingsForm", "До количества очков"))
        self.label_end_game.setText(_translate("SettingsForm", "Окончание игры"))
        self.label_cost_question_group.setText(_translate("SettingsForm", "Стоимость вопроса"))
        self.radioButton_always_one.setText(_translate("SettingsForm", "Всегда 1 очко"))
        self.radioButton_store_price.setText(_translate("SettingsForm", "Накапливается за не отвеченные вопросы"))
        self.radioButton_add_cost_answer.setText(_translate("SettingsForm", "Указывать вручную"))
        self.label_two_answers.setText(_translate("SettingsForm", "Одновременный ответ"))
        self.radioButton_draw_choice.setText(_translate("SettingsForm", "Бросать жребий вручную"))
        self.radioButton_draw_auto.setText(_translate("SettingsForm", "Бросать жребий автоматически"))
        self.label_score_group_2.setText(_translate("SettingsForm", "Счёт"))
        self.radioButton_score_auto_2.setText(_translate("SettingsForm", "Вёдётся автоматически"))
        self.radioButton_score_not_2.setText(_translate("SettingsForm", "Не ведётся"))
        self.checkBox_score_fine_2.setText(_translate("SettingsForm", "Неверный ответ штрафуется"))
        self.checkBox_score_clear_2.setText(_translate("SettingsForm", "Сбрасывать в начале раунда"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScore), _translate("SettingsForm", "Счёт"))
        self.radioButton_falsestart_off.setText(_translate("SettingsForm", "Отсутствует"))
        self.radioButton_falsestart_equal_wrong_answer.setText(_translate("SettingsForm", "Считается неверным ответом"))
        self.checkBox_falsestart_ignore_time_button.setText(_translate("SettingsForm", "Нажатие кнопки “Время” игнорируется в течение"))
        self.label_false_seconds.setText(_translate("SettingsForm", "сек"))
        self.checkBox_ignore_last_team_falsestart.setText(_translate("SettingsForm", "Игнорировать фальстарт последней команды"))
        self.radioButton_falsestart_block_team_button.setText(_translate("SettingsForm", "Блокируется"))
        self.checkBox_falsestart_block_team_button.setText(_translate("SettingsForm", "Штраф - Блокировка кнопки на "))
        self.label_false_block_seconds.setText(_translate("SettingsForm", "сек"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFalsestart), _translate("SettingsForm", "Фальстарт"))
        self.checkBox_keep_game_protocol.setText(_translate("SettingsForm", "Вести протокол игры"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProtocol), _translate("SettingsForm", "Протокол"))
        self.pushButton_default.setText(_translate("SettingsForm", "По умолчанию"))
        self.pushButton_save.setText(_translate("SettingsForm", "Сохранить"))
        self.pushButton_download.setText(_translate("SettingsForm", "Загрузить"))
        self.pushButton_apply.setText(_translate("SettingsForm", "Применить"))
        self.pushButton_cansel.setText(_translate("SettingsForm", "Отмена"))