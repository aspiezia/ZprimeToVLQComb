def get_model():
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/theta_1_0p0_0p0_1p0.root', include_mc_uncertainties = True)#mc uncertainties=true
    model.fill_histogram_zerobins()
    model.set_signal_processes('signal*')
    #model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    #model.add_lognormal_uncertainty('qcd_rate', math.log(1.15), 'qcd')
    for p in model.processes:
        if p == 'qcd': continue
        model.add_lognormal_uncertainty('lumi', math.log(1.027), p)
        model.add_lognormal_uncertainty('trigger', math.log(1.03), p)
        #if 'signal' in p:
        #    model.add_lognormal_uncertainty(p+'_rate', math.log(1.15), p)
    return model
model = get_model()
model_summary(model)
options = Options()
options.set('main', 'n_threads', '20')
#plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'
plot_exp, plot_obs = bayesian_limits(model,what='all')#bayesian_limits ,what='expected'
plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp_1_0p0_0p0_1p0.txt')
plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs_1_0p0_0p0_1p0.txt')
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/htmlout_1_0p0_0p0_1p0')