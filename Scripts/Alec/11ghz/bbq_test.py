''' Testing the BBQ code
    @author: Alec
'''
#Note: Not sure exactly what imports I need
import bbq
from hfss import load_HFSS_project

### Design
project_path = r'C:\Users\rslqulab\Desktop\Alec\\'
project_name = r'11ghz_alec'
design_name  = r'11ghz_design1'

### Junction Parameters
junc_rects    = ['top_junction','bot_junction']
junc_lines    = ['top_junc_line','bot_junc_line']
junc_LJ_names = ['top_lj','bot_lj']
junc_lens     = [0.0001]*2

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

### Testing with things from Zlatko's code
reload(bbq)
from bbq  import BbqAnalysis
bba = BbqAnalysis(bbp.data_filename)
print "Available variations: ", bba.variations

cos_trunc = 10;   fock_trunc  = 7;
CHI_O1, CHI_ND, PJ, Om, EJ, diff, LJs, SIGN, f0s, f1s, fzpfs, Qs, varz = \
    bba.analyze_variation(variation = '0', cos_trunc = cos_trunc,   fock_trunc  = fock_trunc)
s         = sol[variation];   
meta_data = meta_datas[variation]
varz      = hfss_variables[variation]    
CHI_O1, CHI_ND, PJ, Om, EJ, diff, LJs, SIGN, f0s, f1s, fzpfs, Qs = \
    eBBQ_Pmj_to_H_params(s, meta_data, cos_trunc = cos_trunc, fock_trunc = fock_trunc)

print '\nPJ=\t(renorm.)';        print_matrix(PJ*SIGN, frmt = "{:7.4f}")
#print '\nCHI_O1=\t PT. [alpha diag]'; print_matrix(CHI_O1,append_row ="MHz" )
print '\nf0={:6.2f} {:7.2f} {:7.2f} GHz'.format(*f0s)
print '\nCHI_ND=\t PJ O(%d) [alpha diag]'%(cos_trunc); print_matrix(CHI_ND, append_row ="MHz")
print '\nf1={:6.2f} {:7.2f} {:7.2f} GHz'.format(*(f1s*1E-9))   
print 'Q={:8.1e} {:7.1e} {:6.0f}'.format(*(Qs))
print pd.Series({ key:varz[key] for key in ['_join_w','_join_h','_padV_width', '_padV_height','_padH_width', '_padH_height','_scaleV','_scaleH', '_LJ1','_LJ2'] })
