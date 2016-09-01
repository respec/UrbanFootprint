
# UrbanFootprint v1.5
# Copyright (C) 2016 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.

__author__ = 'calthorpe_analytics'


#******************************************************************************
#         Constants
#******************************************************************************

# 1 -- Trip Generations ------------------------
cLogMultiplier_du_det_df = 0.92
cLogMultiplier_emp_retail = 0.65
cLogMultiplier_emp_vmt_office = 0.84
cLogMultiplier_emp_vmt_public = 0.84

cLogConstant_du_det_df = 2.71
cLogConstant_emp_retail = 5.83
cLogConstant_emp_vmt_office = 2.23
cLogConstant_emp_vmt_public = 2.23

cLinearMult_mf2to4 = 6.06
cLinearConst_mf2to4 = 123.56
cLinearMult_mf5p = 3.77
cLinearConst_mf5p = 223.66  ##-- 21mar11
cLinearMult_emp_industry = 2.95
cLinearConst_emp_industry = 30.57

cJobConversionRate = 2

# 2 -- Trip Purpose ------------------------

#      NCHRP Factors
cProd_perc_per_hh = 8.85
cProd_perc_hbw = 0.21
cProd_perc_hbo = 0.5625
cProd_perc_nhb = 0.2275

cAttractions_per_hh_hbw = 0
cAttractions_per_hh_hbo = 0.90
cAttractions_per_hh_nhb = 0.50

cAttractions_per_ret_emp_hbw = 1.45
cAttractions_per_ret_emp_hbo = 9.0
cAttractions_per_ret_emp_nhb = 4.10

cAttractions_per_service_emp_hbw = 1.45
cAttractions_per_service_emp_hbo = 1.70
cAttractions_per_service_emp_nhb = 1.20

cAttractions_per_ind_emp_hbw = 1.45
cAttractions_per_ind_emp_hbo = 0.5
cAttractions_per_ind_emp_nhb = 0.5

#      Other Factors
cProd_school_hbw = 0
cProd_school_hbo = 0
cProd_school_nhb = 0.025

cAttractions_school_hbw = 0.35
cAttractions_school_hbo = 0.60
cAttractions_school_nhb = 0.025

#      Non-home based trips generated by project households
c_nhbtgph_within_project = 0.0
c_nhbtgph_in_to_out_project = 0.0
c_nhbtgph_outside_project = 1.0

# 3 -- Trip Purpose Splits ------------------------

# 4 -- Auto ownership assumptions ------------------------
cAuto_const = 0.2908
cAuto_const_coef = 1.0
cAuto_workers_per_hh_coef = 0.5574
cAuto_non_workers_16_64_hh_coef = 0.3901
cAuto_non_workers_65_hh_coef = 0.3957
cAuto_hh_income_coef = 0.1851
cAuto_hh_income_gt_100k_coef = -0.1865
cAuto_hh_mfdu_coef = -0.2323
cAuto_log_net_hu_dens_coef = -0.0654
cAuto_log_net_retail_dens_coef = -0.0224

cAuto_jobs_45_trans_coef = -0.00000031721


# 5 -- Models Variables ----------------------------------------------------------

cICPM_hbw_107 = -1.75
cICPM_hbo_107 = -2.43
cICPM_nhb_107 = -5.32
cICPM_hbw_108 = None
cICPM_hbo_108 = 0.0
cICPM_nhb_108 = 0.208
cICPM_hbw_109 = None
cICPM_hbo_109 = 0.486  ## 12may11
cICPM_nhb_109 = 0.468
cICPM_hbw_110 = 0.389
cICPM_hbo_110 = 0.399  ## 12may11
cICPM_nhb_110 = None
cICPM_hbw_111 = None
cICPM_hbo_111 = 0.38
cICPM_nhb_111 = None
cICPM_hbw_112 = None
cICPM_hbo_112 = 0.385
cICPM_nhb_112 = 0.638   ##31Oct10 missed term added
cICPM_hbw_113 = -1.33    ##14Dec10 corrected constant
cICPM_hbo_113 = -0.867
cICPM_nhb_113 = -0.237
cICPM_hbw_114 = -0.99
cICPM_hbo_114 = -0.59
cICPM_nhb_114 = -0.163

cWTPM_hbw_121 = -5.55
cWTPM_hbo_121 = -10.96
cWTPM_nhb_121 = -15.09
cWTPM_hbw_122 = None
cWTPM_hbo_122 = -0.415
cWTPM_nhb_122 = None
cWTPM_hbw_123 = None
cWTPM_hbo_123 = 0.37
cWTPM_nhb_123 = 0.377
cWTPM_hbw_124 = 0.226
cWTPM_hbo_124 = 0.219 #13May11
cWTPM_nhb_124 = None
cWTPM_hbw_125 = None
cWTPM_hbo_125 = 0.216
cWTPM_nhb_125 = None
cWTPM_hbw_126 = None
cWTPM_hbo_126 = 0.0
cWTPM_nhb_126 = 0.803
cWTPM_hbw_127 = 0.385
cWTPM_hbo_127 = 0.45
cWTPM_nhb_127 = 0.44
cWTPM_hbw_128 = -1.57
cWTPM_hbo_128 = -0.486
cWTPM_nhb_128 = -0.281
cWTPM_hbw_129 = -1.84
cWTPM_hbo_129 = -0.768
cWTPM_nhb_129 = -0.242

cTTPM_hbw_136 = -8.05
cTTPM_hbo_136 = -6.08
cTTPM_nhb_136 = -2.69
cTTPM_hbw_137 = None
cTTPM_hbo_137 = 0.324
cTTPM_nhb_137 = None
cTTPM_hbw_138 = 1.12
cTTPM_hbo_138 = None
cTTPM_nhb_138 = None
cTTPM_hbw_139 = 0.209
cTTPM_hbo_139 = None
cTTPM_nhb_139 = 0.134
cTTPM_hbw_140 = 0.357
cTTPM_hbo_140 = 0.467
cTTPM_nhb_140 = None
cTTPM_hbw_141 = -1.14
cTTPM_hbo_141 = -0.958
cTTPM_nhb_141 = None
cTTPM_hbw_142 = -1.68
cTTPM_hbo_142 = -1.09
cTTPM_nhb_142 = -0.34

vmt_output_field_list = ['id', 'acres_gross', 'pop', 'du', 'hh', 'emp', 'final_prod_hbo', 'final_prod_hbw', 'final_prod_nhb',
                         'final_attr_hbo', 'final_attr_hbw', 'final_attr_nhb', 'vmt_daily', 'vmt_daily_w_trucks',
                         'vmt_daily_per_capita', 'vmt_daily_per_hh', 'vmt_annual', 'vmt_annual_w_trucks',
                         'vmt_annual_per_capita', 'vmt_annual_per_hh', 'raw_trips_total', 'internal_capture_trips_total',
                         'walking_trips_total', 'transit_trips_total']