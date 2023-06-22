:py:mod:`porf.run_analyser`
===========================

.. py:module:: porf.run_analyser


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   porf.run_analyser.RunAnalyser




.. py:class:: RunAnalyser(run_directory=None)

   This class aims to list and perform analysis on all the relevant files in a particular run between all the corners.

   .. py:method:: get_all_rpt_files()


   .. py:method:: extract_metrics_timing()

      For every file in the sta timing file, extract the propagation delay and save the file meta data into a dicitonary.


   .. py:method:: extract_metrics_power()



