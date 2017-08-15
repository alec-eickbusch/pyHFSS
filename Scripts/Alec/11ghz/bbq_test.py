''' Testing the BBQ code
    @author: Alec
'''
#Note: Not sure exactly what imports I need
import bbq
from hfss import CalcObject, ureg, load_HFSS_project, get_active_project

### Design
project_path = r'C:\Users\rslqulab\Desktop\Alec\\'
project_name = r'11ghz_alec'
design_name  = r'11ghz_design1'

### Junction Parameters
junc_rects    = ['top_junc','bot_junc']
junc_lines    = ['top_junc_line','bot_junc_line']
junc_LJ_names = ['top_lj','bot_lj']
junc_lens     = [0.0001]

### Connecting to HFSS and running
app, desktop, project = load_HFSS_project(project_name, project_path)
design                = project.get_design(design_name)

### Doing BBQ
bbp = bbq.Bbq(project, design, append_analysis=False)
bbp.do_eBBQ(junc_rect=junc_rects, junc_lines = junc_lines, junc_len = junc_lens, junc_LJ_var_name = junc_LJ_names)

### Collect results
bba            = bbp.bbq_analysis
sol            = bba.sols
meta_datas     = bba.meta_data
hfss_variables = bba.hfss_variables

 
