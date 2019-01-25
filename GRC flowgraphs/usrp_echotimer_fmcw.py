#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Echotimer Fmcw
# Generated: Fri Dec 21 15:55:12 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import radar
import sip
import sys
from gnuradio import qtgui


class usrp_echotimer_fmcw(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Echotimer Fmcw")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Usrp Echotimer Fmcw")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "usrp_echotimer_fmcw")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_up = samp_up = 1250000/4
        self.samp_rate = samp_rate = 5000000
        self.sweep_freq = sweep_freq = samp_rate/2
        self.samp_down = samp_down = samp_up
        self.samp_cw = samp_cw = 1250000
        self.center_freq = center_freq = 2.4e9
        self.wait_to_start = wait_to_start = 0.05
        self.v_res_m_s = v_res_m_s = samp_rate/samp_cw*3e8/2/center_freq
        self.tx_gain = tx_gain = 55
        self.threshold = threshold = -150
        self.rx_gain = rx_gain = 55
        self.range_res_m = range_res_m = 3e8/2/sweep_freq
        self.protect_samp = protect_samp = 0
        self.min_output_buffer = min_output_buffer = int((samp_up+samp_down+samp_cw)*2)
        self.meas_duration = meas_duration = (samp_cw+samp_up+samp_down)/float(samp_rate)
        self.max_output_buffer = max_output_buffer = 0
        self.freq_res_up = freq_res_up = samp_rate/samp_up
        self.freq_res_cw = freq_res_cw = samp_rate/samp_cw
        self.delay_samp = delay_samp = 61
        self.decim_fac = decim_fac = 5**4
        self.b210 = b210 = "A:B"

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 70, 1, 55, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 0,0)
        self._threshold_range = Range(-200, 0, 1, -150, 200)
        self._threshold_win = RangeWidget(self._threshold_range, self.set_threshold, "threshold", "counter_slider", float)
        self.top_grid_layout.addWidget(self._threshold_win, 1,0)
        self._rx_gain_range = Range(0, 70, 1, 55, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 0,1)
        self._protect_samp_range = Range(0, 100, 1, 0, 200)
        self._protect_samp_win = RangeWidget(self._protect_samp_range, self.set_protect_samp, "protect_samp", "counter_slider", float)
        self.top_grid_layout.addWidget(self._protect_samp_win, 1,1)
        self._delay_samp_range = Range(0, 100, 1, 61, 200)
        self._delay_samp_win = RangeWidget(self._delay_samp_range, self.set_delay_samp, 'Number delay samples', "counter_slider", float)
        self.top_layout.addWidget(self._delay_samp_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim_fac,
                taps=None,
                fractional_bw=None,
        )
        self.radar_usrp_echotimer_cc_0 = radar.usrp_echotimer_cc(samp_rate, center_freq, int(delay_samp), '', '', 'internal', 'none', 'TX/RX', tx_gain, 0.1, wait_to_start, 0, '', '', 'internal', 'none', 'RX2', rx_gain, 0.1, wait_to_start, 0, "packet_len")
        (self.radar_usrp_echotimer_cc_0).set_min_output_buffer(3750000)
        self.radar_ts_fft_cc_2 = radar.ts_fft_cc(samp_down/decim_fac,  "packet_len")
        self.radar_ts_fft_cc_1 = radar.ts_fft_cc(samp_up/decim_fac,  "packet_len")
        self.radar_ts_fft_cc_0 = radar.ts_fft_cc(samp_cw/decim_fac,  "packet_len")
        self.radar_tracking_singletarget_0 = radar.tracking_singletarget(500, 1, v_res_m_s, 0.01, 0.001, 1, "kalman")
        self.radar_split_cc_0_0_0 = radar.split_cc(2, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0_0_0).set_min_output_buffer(3750000)
        self.radar_split_cc_0_0 = radar.split_cc(1, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0_0).set_min_output_buffer(3750000)
        self.radar_split_cc_0 = radar.split_cc(0, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0).set_min_output_buffer(3750000)
        self.radar_signal_generator_fmcw_c_0 = radar.signal_generator_fmcw_c(samp_rate, samp_up, samp_down, samp_cw, -(sweep_freq)/2, sweep_freq, 0.5, "packet_len")
        (self.radar_signal_generator_fmcw_c_0).set_min_output_buffer(3750000)
        self.radar_qtgui_time_plot_0_0 = radar.qtgui_time_plot(100, "velocity", (-2,2), 60, "TRACKING")
        self.radar_qtgui_time_plot_0 = radar.qtgui_time_plot(100, "range", (0,20), 60, "TRACKING")
        self.radar_print_results_0 = radar.print_results(False, "")
        self.radar_find_max_peak_c_0_0_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0_0_0).set_min_output_buffer(3750000)
        self.radar_find_max_peak_c_0_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0_0).set_min_output_buffer(3750000)
        self.radar_find_max_peak_c_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0).set_min_output_buffer(3750000)
        self.radar_estimator_fmcw_0 = radar.estimator_fmcw(samp_rate/decim_fac, center_freq, sweep_freq, samp_up/decim_fac, samp_down/decim_fac, False)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_c(
        	samp_up/decim_fac, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim_fac, #bw
        	'DOWN', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_0_0_win)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)



        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	samp_up/decim_fac, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim_fac, #bw
        	'UP', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)



        self.qtgui_sink_x_0 = qtgui.sink_c(
        	samp_cw/decim_fac, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim_fac, #bw
        	"CW", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, "packet_len", 1.0/decim_fac)
        (self.blocks_tagged_stream_multiply_length_0).set_min_output_buffer(3750000)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        (self.blocks_multiply_conjugate_cc_0).set_min_output_buffer(3750000)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.radar_estimator_fmcw_0, 'Msg out'), (self.radar_print_results_0, 'Msg in'))
        self.msg_connect((self.radar_estimator_fmcw_0, 'Msg out'), (self.radar_tracking_singletarget_0, 'Msg in'))
        self.msg_connect((self.radar_find_max_peak_c_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in CW'))
        self.msg_connect((self.radar_find_max_peak_c_0_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in UP'))
        self.msg_connect((self.radar_find_max_peak_c_0_0_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in DOWN'))
        self.msg_connect((self.radar_tracking_singletarget_0, 'Msg out'), (self.radar_qtgui_time_plot_0, 'Msg in'))
        self.msg_connect((self.radar_tracking_singletarget_0, 'Msg out'), (self.radar_qtgui_time_plot_0_0, 'Msg in'))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0_0_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.radar_usrp_echotimer_cc_0, 0))
        self.connect((self.radar_split_cc_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.radar_split_cc_0, 0), (self.radar_ts_fft_cc_0, 0))
        self.connect((self.radar_split_cc_0_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.radar_split_cc_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.radar_split_cc_0_0, 0), (self.radar_ts_fft_cc_1, 0))
        self.connect((self.radar_split_cc_0_0_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.radar_split_cc_0_0_0, 0), (self.radar_ts_fft_cc_2, 0))
        self.connect((self.radar_ts_fft_cc_0, 0), (self.radar_find_max_peak_c_0, 0))
        self.connect((self.radar_ts_fft_cc_1, 0), (self.radar_find_max_peak_c_0_0, 0))
        self.connect((self.radar_ts_fft_cc_2, 0), (self.radar_find_max_peak_c_0_0_0, 0))
        self.connect((self.radar_usrp_echotimer_cc_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "usrp_echotimer_fmcw")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_up(self):
        return self.samp_up

    def set_samp_up(self, samp_up):
        self.samp_up = samp_up
        self.set_samp_down(self.samp_up)
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_up(self.samp_rate/self.samp_up)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_v_res_m_s(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.set_sweep_freq(self.samp_rate/2)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_up(self.samp_rate/self.samp_up)
        self.set_freq_res_cw(self.samp_rate/self.samp_cw)

    def get_sweep_freq(self):
        return self.sweep_freq

    def set_sweep_freq(self, sweep_freq):
        self.sweep_freq = sweep_freq
        self.set_range_res_m(3e8/2/self.sweep_freq)

    def get_samp_down(self):
        return self.samp_down

    def set_samp_down(self, samp_down):
        self.samp_down = samp_down
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))

    def get_samp_cw(self):
        return self.samp_cw

    def set_samp_cw(self, samp_cw):
        self.samp_cw = samp_cw
        self.set_v_res_m_s(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_cw(self.samp_rate/self.samp_cw)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_v_res_m_s(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)

    def get_wait_to_start(self):
        return self.wait_to_start

    def set_wait_to_start(self, wait_to_start):
        self.wait_to_start = wait_to_start

    def get_v_res_m_s(self):
        return self.v_res_m_s

    def set_v_res_m_s(self, v_res_m_s):
        self.v_res_m_s = v_res_m_s

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.radar_usrp_echotimer_cc_0.set_tx_gain(self.tx_gain)

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.radar_find_max_peak_c_0_0_0.set_threshold(self.threshold)
        self.radar_find_max_peak_c_0_0.set_threshold(self.threshold)
        self.radar_find_max_peak_c_0.set_threshold(self.threshold)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.radar_usrp_echotimer_cc_0.set_rx_gain(self.rx_gain)

    def get_range_res_m(self):
        return self.range_res_m

    def set_range_res_m(self, range_res_m):
        self.range_res_m = range_res_m

    def get_protect_samp(self):
        return self.protect_samp

    def set_protect_samp(self, protect_samp):
        self.protect_samp = protect_samp
        self.radar_find_max_peak_c_0_0_0.set_samp_protect(int(self.protect_samp))
        self.radar_find_max_peak_c_0_0.set_samp_protect(int(self.protect_samp))
        self.radar_find_max_peak_c_0.set_samp_protect(int(self.protect_samp))

    def get_min_output_buffer(self):
        return self.min_output_buffer

    def set_min_output_buffer(self, min_output_buffer):
        self.min_output_buffer = min_output_buffer

    def get_meas_duration(self):
        return self.meas_duration

    def set_meas_duration(self, meas_duration):
        self.meas_duration = meas_duration

    def get_max_output_buffer(self):
        return self.max_output_buffer

    def set_max_output_buffer(self, max_output_buffer):
        self.max_output_buffer = max_output_buffer

    def get_freq_res_up(self):
        return self.freq_res_up

    def set_freq_res_up(self, freq_res_up):
        self.freq_res_up = freq_res_up

    def get_freq_res_cw(self):
        return self.freq_res_cw

    def set_freq_res_cw(self, freq_res_cw):
        self.freq_res_cw = freq_res_cw

    def get_delay_samp(self):
        return self.delay_samp

    def set_delay_samp(self, delay_samp):
        self.delay_samp = delay_samp
        self.radar_usrp_echotimer_cc_0.set_num_delay_samps(int(self.delay_samp))

    def get_decim_fac(self):
        return self.decim_fac

    def set_decim_fac(self, decim_fac):
        self.decim_fac = decim_fac
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(1.0/self.decim_fac)

    def get_b210(self):
        return self.b210

    def set_b210(self, b210):
        self.b210 = b210


def main(top_block_cls=usrp_echotimer_fmcw, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
