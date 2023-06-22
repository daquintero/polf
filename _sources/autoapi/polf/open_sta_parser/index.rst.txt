:py:mod:`porf.open_sta_parser`
==============================

.. py:module:: porf.open_sta_parser


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   porf.open_sta_parser.OpenSTAParser




.. py:class:: OpenSTAParser(file_address='25-rcx_sta.rpt')

   Methodology:
   1. Read metadata on the type of file and run this is.
   2. Identify the boundary lines of the table data through regex matching.
   3. Read in table data of the timing performance.
   4. Understand the relevant timing and data parameters.
   5. Extract the relevant timing and data parameters from the

   .. py:method:: read_file_meta_data()


   .. py:method:: configure_frame_id()


   .. py:method:: configure_timing_data_rows()


   .. py:method:: extract_frame_meta_data()


   .. py:method:: extract_timing_data(frame_id=0)


   .. py:method:: calculate_propagation_delay(net_name_in='in', net_name_out='out', timing_data=None)



