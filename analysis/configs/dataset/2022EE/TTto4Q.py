from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="TTto4Q",
    path=(
        "root://maite.iihe.ac.be:1094//store/user/daocampo/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2_BTV_Run3_2022_Comm_MINIAODv4/240515_152854/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=762.1,
    partitions=25,
    stepsize=50_000,
    filenames=(
        "MC_defaultAK4_587.root",
        "MC_defaultAK4_538.root",
        "MC_defaultAK4_418.root",
        "MC_defaultAK4_110.root",
        "MC_defaultAK4_111.root",
        "MC_defaultAK4_592.root",
        "MC_defaultAK4_497.root",
        "MC_defaultAK4_593.root",
        "MC_defaultAK4_755.root",
        "MC_defaultAK4_76.root",
        "MC_defaultAK4_589.root",
        "MC_defaultAK4_72.root",
        "MC_defaultAK4_71.root",
        "MC_defaultAK4_101.root",
        "MC_defaultAK4_108.root",
        "MC_defaultAK4_651.root",
        "MC_defaultAK4_657.root",
        "MC_defaultAK4_659.root",
        "MC_defaultAK4_655.root",
        "MC_defaultAK4_590.root",
        "MC_defaultAK4_660.root",
        "MC_defaultAK4_74.root",
        "MC_defaultAK4_106.root",
        "MC_defaultAK4_65.root",
        "MC_defaultAK4_109.root",
        "MC_defaultAK4_202.root",
        "MC_defaultAK4_116.root",
        "MC_defaultAK4_117.root",
        "MC_defaultAK4_662.root",
        "MC_defaultAK4_539.root",
        "MC_defaultAK4_658.root",
        "MC_defaultAK4_104.root",
        "MC_defaultAK4_75.root",
        "MC_defaultAK4_540.root",
        "MC_defaultAK4_156.root",
        "MC_defaultAK4_600.root",
        "MC_defaultAK4_204.root",
        "MC_defaultAK4_23.root",
        "MC_defaultAK4_230.root",
        "MC_defaultAK4_129.root",
        "MC_defaultAK4_154.root",
        "MC_defaultAK4_121.root",
        "MC_defaultAK4_205.root",
        "MC_defaultAK4_113.root",
        "MC_defaultAK4_107.root",
        "MC_defaultAK4_543.root",
        "MC_defaultAK4_127.root",
        "MC_defaultAK4_544.root",
        "MC_defaultAK4_588.root",
        "MC_defaultAK4_608.root",
        "MC_defaultAK4_603.root",
        "MC_defaultAK4_21.root",
        "MC_defaultAK4_607.root",
        "MC_defaultAK4_118.root",
        "MC_defaultAK4_66.root",
        "MC_defaultAK4_77.root",
        "MC_defaultAK4_119.root",
        "MC_defaultAK4_124.root",
        "MC_defaultAK4_16.root",
        "MC_defaultAK4_601.root",
        "MC_defaultAK4_128.root",
        "MC_defaultAK4_654.root",
        "MC_defaultAK4_24.root",
        "MC_defaultAK4_591.root",
        "MC_defaultAK4_10.root",
        "MC_defaultAK4_606.root",
        "MC_defaultAK4_12.root",
        "MC_defaultAK4_208.root",
        "MC_defaultAK4_112.root",
        "MC_defaultAK4_115.root",
        "MC_defaultAK4_17.root",
        "MC_defaultAK4_542.root",
        "MC_defaultAK4_611.root",
        "MC_defaultAK4_125.root",
        "MC_defaultAK4_78.root",
        "MC_defaultAK4_665.root",
        "MC_defaultAK4_79.root",
        "MC_defaultAK4_25.root",
        "MC_defaultAK4_546.root",
        "MC_defaultAK4_123.root",
        "MC_defaultAK4_545.root",
        "MC_defaultAK4_14.root",
        "MC_defaultAK4_609.root",
        "MC_defaultAK4_496.root",
        "MC_defaultAK4_126.root",
        "MC_defaultAK4_602.root",
        "MC_defaultAK4_668.root",
        "MC_defaultAK4_155.root",
        "MC_defaultAK4_494.root",
        "MC_defaultAK4_656.root",
        "MC_defaultAK4_495.root",
        "MC_defaultAK4_114.root",
        "MC_defaultAK4_165.root",
        "MC_defaultAK4_18.root",
        "MC_defaultAK4_11.root",
        "MC_defaultAK4_19.root",
        "MC_defaultAK4_571.root",
        "MC_defaultAK4_493.root",
        "MC_defaultAK4_613.root",
        "MC_defaultAK4_162.root",
        "MC_defaultAK4_732.root",
        "MC_defaultAK4_615.root",
        "MC_defaultAK4_20.root",
        "MC_defaultAK4_27.root",
        "MC_defaultAK4_157.root",
        "MC_defaultAK4_28.root",
        "MC_defaultAK4_159.root",
        "MC_defaultAK4_573.root",
        "MC_defaultAK4_161.root",
        "MC_defaultAK4_620.root",
        "MC_defaultAK4_120.root",
        "MC_defaultAK4_175.root",
        "MC_defaultAK4_173.root",
        "MC_defaultAK4_467.root",
        "MC_defaultAK4_103.root",
        "MC_defaultAK4_160.root",
        "MC_defaultAK4_62.root",
        "MC_defaultAK4_22.root",
        "MC_defaultAK4_200.root",
        "MC_defaultAK4_575.root",
        "MC_defaultAK4_26.root",
        "MC_defaultAK4_70.root",
        "MC_defaultAK4_541.root",
        "MC_defaultAK4_490.root",
        "MC_defaultAK4_203.root",
        "MC_defaultAK4_67.root",
        "MC_defaultAK4_122.root",
        "MC_defaultAK4_572.root",
        "MC_defaultAK4_491.root",
        "MC_defaultAK4_466.root",
        "MC_defaultAK4_209.root",
        "MC_defaultAK4_754.root",
        "MC_defaultAK4_577.root",
        "MC_defaultAK4_60.root",
        "MC_defaultAK4_201.root",
        "MC_defaultAK4_13.root",
        "MC_defaultAK4_15.root",
        "MC_defaultAK4_738.root",
        "MC_defaultAK4_739.root",
        "MC_defaultAK4_736.root",
        "MC_defaultAK4_29.root",
        "MC_defaultAK4_619.root",
        "MC_defaultAK4_737.root",
        "MC_defaultAK4_626.root",
        "MC_defaultAK4_621.root",
        "MC_defaultAK4_670.root",
        "MC_defaultAK4_64.root",
        "MC_defaultAK4_622.root",
        "MC_defaultAK4_612.root",
        "MC_defaultAK4_61.root",
        "MC_defaultAK4_63.root",
        "MC_defaultAK4_68.root",
        "MC_defaultAK4_207.root",
        "MC_defaultAK4_105.root",
        "MC_defaultAK4_69.root",
        "MC_defaultAK4_661.root",
        "MC_defaultAK4_652.root",
        "MC_defaultAK4_666.root",
        "MC_defaultAK4_664.root",
        "MC_defaultAK4_73.root",
        "MC_defaultAK4_102.root",
        "MC_defaultAK4_663.root",
        "MC_defaultAK4_653.root",
        "MC_defaultAK4_650.root",
        "MC_defaultAK4_667.root",
        "MC_defaultAK4_674.root",
        "MC_defaultAK4_231.root",
        "MC_defaultAK4_206.root",
        "MC_defaultAK4_153.root",
        "MC_defaultAK4_730.root",
        "MC_defaultAK4_610.root",
        "MC_defaultAK4_170.root",
        "MC_defaultAK4_158.root",
        "MC_defaultAK4_604.root",
        "MC_defaultAK4_605.root",
        "MC_defaultAK4_614.root",
        "MC_defaultAK4_617.root",
        "MC_defaultAK4_163.root",
        "MC_defaultAK4_171.root",
        "MC_defaultAK4_547.root",
        "MC_defaultAK4_702.root",
        "MC_defaultAK4_673.root",
        "MC_defaultAK4_700.root",
        "MC_defaultAK4_704.root",
        "MC_defaultAK4_574.root",
        "MC_defaultAK4_669.root",
        "MC_defaultAK4_576.root",
        "MC_defaultAK4_624.root",
        "MC_defaultAK4_616.root",
        "MC_defaultAK4_752.root",
        "MC_defaultAK4_166.root",
        "MC_defaultAK4_172.root",
        "MC_defaultAK4_618.root",
        "MC_defaultAK4_570.root",
        "MC_defaultAK4_731.root",
        "MC_defaultAK4_234.root",
        "MC_defaultAK4_733.root",
        "MC_defaultAK4_232.root",
        "MC_defaultAK4_1-23.root",
        "MC_defaultAK4_625.root",
        "MC_defaultAK4_1-34.root",
        "MC_defaultAK4_240.root",
        "MC_defaultAK4_243.root",
        "MC_defaultAK4_151.root",
        "MC_defaultAK4_748.root",
        "MC_defaultAK4_750.root",
        "MC_defaultAK4_235.root",
        "MC_defaultAK4_164.root",
        "MC_defaultAK4_176.root",
        "MC_defaultAK4_168.root",
        "MC_defaultAK4_167.root",
        "MC_defaultAK4_734.root",
        "MC_defaultAK4_735.root",
        "MC_defaultAK4_178.root",
        "MC_defaultAK4_623.root",
        "MC_defaultAK4_492.root",
        "MC_defaultAK4_241.root",
        "MC_defaultAK4_169.root",
        "MC_defaultAK4_703.root",
        "MC_defaultAK4_499.root",
        "MC_defaultAK4_498.root",
        "MC_defaultAK4_238.root",
        "MC_defaultAK4_239.root",
        "MC_defaultAK4_741.root",
        "MC_defaultAK4_742.root",
        "MC_defaultAK4_740.root",
        "MC_defaultAK4_672.root",
        "MC_defaultAK4_245.root",
        "MC_defaultAK4_1-35.root",
        "MC_defaultAK4_548.root",
        "MC_defaultAK4_1-29.root",
        "MC_defaultAK4_1-30.root",
        "MC_defaultAK4_747.root",
        "MC_defaultAK4_744.root",
        "MC_defaultAK4_745.root",
        "MC_defaultAK4_743.root",
        "MC_defaultAK4_1-27.root",
        "MC_defaultAK4_749.root",
        "MC_defaultAK4_1-28.root",
        "MC_defaultAK4_174.root",
        "MC_defaultAK4_177.root",
        "MC_defaultAK4_751.root",
        "MC_defaultAK4_746.root",
        "MC_defaultAK4_1-33.root",
        "MC_defaultAK4_708.root",
        "MC_defaultAK4_1-1.root",
        "MC_defaultAK4_236.root",
        "MC_defaultAK4_1-25.root",
        "MC_defaultAK4_709.root",
        "MC_defaultAK4_1-21.root",
        "MC_defaultAK4_1-20.root",
        "MC_defaultAK4_1-26.root",
        "MC_defaultAK4_1-4.root",
        "MC_defaultAK4_1-2.root",
        "MC_defaultAK4_628.root",
        "MC_defaultAK4_248.root",
        "MC_defaultAK4_1-32.root",
        "MC_defaultAK4_246.root",
        "MC_defaultAK4_152.root",
        "MC_defaultAK4_1-3.root",
        "MC_defaultAK4_150.root",
        "MC_defaultAK4_1-9.root",
        "MC_defaultAK4_1-6.root",
        "MC_defaultAK4_705.root",
        "MC_defaultAK4_701.root",
        "MC_defaultAK4_233.root",
        "MC_defaultAK4_706.root",
        "MC_defaultAK4_707.root",
        "MC_defaultAK4_244.root",
        "MC_defaultAK4_1-5.root",
        "MC_defaultAK4_247.root",
        "MC_defaultAK4_671.root",
        "MC_defaultAK4_1-22.root",
        "MC_defaultAK4_1-31.root",
        "MC_defaultAK4_1-8.root",
        "MC_defaultAK4_1-7.root",
        "MC_defaultAK4_251.root",
        "MC_defaultAK4_252.root",
        "MC_defaultAK4_255.root",
        "MC_defaultAK4_627.root",
        "MC_defaultAK4_237.root",
        "MC_defaultAK4_242.root",
        "MC_defaultAK4_254.root",
        "MC_defaultAK4_258.root",
        "MC_defaultAK4_250.root",
        "MC_defaultAK4_257.root",
        "MC_defaultAK4_256.root",
        "MC_defaultAK4_253.root",
        "MC_defaultAK4_249.root",
        "MC_defaultAK4_259.root",
        "MC_defaultAK4_419.root",
        "MC_defaultAK4_1-24.root",
        "MC_defaultAK4_284.root",
        "MC_defaultAK4_286.root",
        "MC_defaultAK4_288.root",
        "MC_defaultAK4_283.root",
        "MC_defaultAK4_282.root",
        "MC_defaultAK4_290.root",
        "MC_defaultAK4_281.root",
        "MC_defaultAK4_297.root",
        "MC_defaultAK4_293.root",
        "MC_defaultAK4_280.root",
        "MC_defaultAK4_295.root",
        "MC_defaultAK4_292.root",
        "MC_defaultAK4_291.root",
        "MC_defaultAK4_287.root",
        "MC_defaultAK4_285.root",
        "MC_defaultAK4_629.root",
        "MC_defaultAK4_296.root",
        "MC_defaultAK4_299.root",
        "MC_defaultAK4_520.root",
        "MC_defaultAK4_294.root",
        "MC_defaultAK4_314.root",
        "MC_defaultAK4_521.root",
        "MC_defaultAK4_523.root",
        "MC_defaultAK4_525.root",
        "MC_defaultAK4_526.root",
        "MC_defaultAK4_522.root",
        "MC_defaultAK4_524.root",
        "MC_defaultAK4_527.root",
        "MC_defaultAK4_528.root",
        "MC_defaultAK4_289.root",
        "MC_defaultAK4_315.root",
        "MC_defaultAK4_311.root",
        "MC_defaultAK4_310.root",
        "MC_defaultAK4_529.root",
        "MC_defaultAK4_530.root",
        "MC_defaultAK4_313.root",
        "MC_defaultAK4_537.root",
        "MC_defaultAK4_326.root",
        "MC_defaultAK4_318.root",
        "MC_defaultAK4_531.root",
        "MC_defaultAK4_532.root",
        "MC_defaultAK4_316.root",
        "MC_defaultAK4_533.root",
        "MC_defaultAK4_323.root",
        "MC_defaultAK4_319.root",
        "MC_defaultAK4_324.root",
        "MC_defaultAK4_312.root",
        "MC_defaultAK4_320.root",
        "MC_defaultAK4_534.root",
        "MC_defaultAK4_535.root",
        "MC_defaultAK4_327.root",
        "MC_defaultAK4_322.root",
        "MC_defaultAK4_2-10.root",
        "MC_defaultAK4_2-11.root",
        "MC_defaultAK4_325.root",
        "MC_defaultAK4_298.root",
        "MC_defaultAK4_321.root",
        "MC_defaultAK4_331.root",
        "MC_defaultAK4_317.root",
        "MC_defaultAK4_339.root",
        "MC_defaultAK4_536.root",
        "MC_defaultAK4_333.root",
        "MC_defaultAK4_335.root",
        "MC_defaultAK4_2-51.root",
        "MC_defaultAK4_328.root",
        "MC_defaultAK4_2-49.root",
        "MC_defaultAK4_2-48.root",
        "MC_defaultAK4_2-57.root",
        "MC_defaultAK4_337.root",
        "MC_defaultAK4_332.root",
        "MC_defaultAK4_334.root",
        "MC_defaultAK4_2-50.root",
        "MC_defaultAK4_329.root",
        "MC_defaultAK4_2-14.root",
        "MC_defaultAK4_2-12.root",
        "MC_defaultAK4_2-16.root",
        "MC_defaultAK4_2-18.root",
        "MC_defaultAK4_2-13.root",
        "MC_defaultAK4_2-19.root",
        "MC_defaultAK4_2-17.root",
        "MC_defaultAK4_2-15.root",
        "MC_defaultAK4_338.root",
        "MC_defaultAK4_2-58.root",
        "MC_defaultAK4_2-61.root",
        "MC_defaultAK4_2-41.root",
        "MC_defaultAK4_2-43.root",
        "MC_defaultAK4_2-42.root",
        "MC_defaultAK4_2-47.root",
        "MC_defaultAK4_2-46.root",
        "MC_defaultAK4_2-45.root",
        "MC_defaultAK4_2-52.root",
        "MC_defaultAK4_2-40.root",
        "MC_defaultAK4_2-44.root",
        "MC_defaultAK4_2-54.root",
        "MC_defaultAK4_2-64.root",
        "MC_defaultAK4_2-53.root",
        "MC_defaultAK4_2-55.root",
        "MC_defaultAK4_2-59.root",
        "MC_defaultAK4_330.root",
        "MC_defaultAK4_2-63.root",
        "MC_defaultAK4_440.root",
        "MC_defaultAK4_369.root",
        "MC_defaultAK4_336.root",
        "MC_defaultAK4_364.root",
        "MC_defaultAK4_2-62.root",
        "MC_defaultAK4_2-56.root",
        "MC_defaultAK4_2-60.root",
        "MC_defaultAK4_365.root",
        "MC_defaultAK4_377.root",
        "MC_defaultAK4_360.root",
        "MC_defaultAK4_363.root",
        "MC_defaultAK4_374.root",
        "MC_defaultAK4_361.root",
        "MC_defaultAK4_378.root",
        "MC_defaultAK4_362.root",
        "MC_defaultAK4_366.root",
        "MC_defaultAK4_367.root",
        "MC_defaultAK4_370.root",
        "MC_defaultAK4_444.root",
        "MC_defaultAK4_371.root",
        "MC_defaultAK4_373.root",
        "MC_defaultAK4_380.root",
        "MC_defaultAK4_372.root",
        "MC_defaultAK4_375.root",
        "MC_defaultAK4_376.root",
        "MC_defaultAK4_446.root",
        "MC_defaultAK4_441.root",
        "MC_defaultAK4_179.root",
        "MC_defaultAK4_2-65.root",
        "MC_defaultAK4_675.root",
        "MC_defaultAK4_594.root",
        "MC_defaultAK4_549.root",
        "MC_defaultAK4_468.root",
        "MC_defaultAK4_30.root",
        "MC_defaultAK4_2-66.root",
        "MC_defaultAK4_676.root",
        "MC_defaultAK4_595.root",
        "MC_defaultAK4_469.root",
        "MC_defaultAK4_31.root",
        "MC_defaultAK4_2-67.root",
        "MC_defaultAK4_677.root",
        "MC_defaultAK4_596.root",
        "MC_defaultAK4_32.root",
        "MC_defaultAK4_2-68.root",
        "MC_defaultAK4_678.root",
        "MC_defaultAK4_597.root",
        "MC_defaultAK4_33.root",
        "MC_defaultAK4_2-69.root",
        "MC_defaultAK4_598.root",
        "MC_defaultAK4_34.root",
        "MC_defaultAK4_599.root",
        "MC_defaultAK4_80.root",
        "MC_defaultAK4_35.root",
        "MC_defaultAK4_81.root",
        "MC_defaultAK4_36.root",
        "MC_defaultAK4_82.root",
        "MC_defaultAK4_37.root",
        "MC_defaultAK4_83.root",
        "MC_defaultAK4_38.root",
        "MC_defaultAK4_84.root",
        "MC_defaultAK4_39.root",
        "MC_defaultAK4_85.root",
        "MC_defaultAK4_86.root",
        "MC_defaultAK4_1.root",
        "MC_defaultAK4_87.root",
        "MC_defaultAK4_2.root",
        "MC_defaultAK4_88.root",
        "MC_defaultAK4_3.root",
        "MC_defaultAK4_89.root",
        "MC_defaultAK4_4.root",
        "MC_defaultAK4_210.root",
        "MC_defaultAK4_5.root",
        "MC_defaultAK4_211.root",
        "MC_defaultAK4_130.root",
        "MC_defaultAK4_6.root",
        "MC_defaultAK4_500.root",
        "MC_defaultAK4_212.root",
        "MC_defaultAK4_131.root",
        "MC_defaultAK4_7.root",
        "MC_defaultAK4_501.root",
        "MC_defaultAK4_420.root",
        "MC_defaultAK4_213.root",
        "MC_defaultAK4_132.root",
        "MC_defaultAK4_8.root",
        "MC_defaultAK4_502.root",
        "MC_defaultAK4_421.root",
        "MC_defaultAK4_340.root",
        "MC_defaultAK4_214.root",
        "MC_defaultAK4_133.root",
        "MC_defaultAK4_9.root",
        "MC_defaultAK4_710.root",
        "MC_defaultAK4_503.root",
        "MC_defaultAK4_422.root",
        "MC_defaultAK4_341.root",
        "MC_defaultAK4_260.root",
        "MC_defaultAK4_215.root",
        "MC_defaultAK4_134.root",
        "MC_defaultAK4_711.root",
        "MC_defaultAK4_2-20.root",
        "MC_defaultAK4_630.root",
        "MC_defaultAK4_504.root",
        "MC_defaultAK4_423.root",
        "MC_defaultAK4_342.root",
        "MC_defaultAK4_261.root",
        "MC_defaultAK4_216.root",
        "MC_defaultAK4_180.root",
        "MC_defaultAK4_135.root",
        "MC_defaultAK4_712.root",
        "MC_defaultAK4_2-21.root",
        "MC_defaultAK4_631.root",
        "MC_defaultAK4_550.root",
        "MC_defaultAK4_505.root",
        "MC_defaultAK4_424.root",
        "MC_defaultAK4_343.root",
        "MC_defaultAK4_262.root",
        "MC_defaultAK4_217.root",
        "MC_defaultAK4_181.root",
        "MC_defaultAK4_136.root",
        "MC_defaultAK4_713.root",
        "MC_defaultAK4_2-22.root",
        "MC_defaultAK4_632.root",
        "MC_defaultAK4_551.root",
        "MC_defaultAK4_506.root",
        "MC_defaultAK4_470.root",
        "MC_defaultAK4_425.root",
        "MC_defaultAK4_344.root",
        "MC_defaultAK4_263.root",
        "MC_defaultAK4_218.root",
        "MC_defaultAK4_182.root",
        "MC_defaultAK4_137.root",
        "MC_defaultAK4_714.root",
        "MC_defaultAK4_2-23.root",
        "MC_defaultAK4_633.root",
        "MC_defaultAK4_552.root",
        "MC_defaultAK4_507.root",
        "MC_defaultAK4_471.root",
        "MC_defaultAK4_426.root",
        "MC_defaultAK4_345.root",
        "MC_defaultAK4_264.root",
        "MC_defaultAK4_219.root",
        "MC_defaultAK4_183.root",
        "MC_defaultAK4_138.root",
        "MC_defaultAK4_715.root",
        "MC_defaultAK4_2-24.root",
        "MC_defaultAK4_634.root",
        "MC_defaultAK4_553.root",
        "MC_defaultAK4_508.root",
        "MC_defaultAK4_472.root",
        "MC_defaultAK4_427.root",
        "MC_defaultAK4_346.root",
        "MC_defaultAK4_265.root",
        "MC_defaultAK4_184.root",
        "MC_defaultAK4_139.root",
        "MC_defaultAK4_716.root",
        "MC_defaultAK4_2-70.root",
        "MC_defaultAK4_2-25.root",
        "MC_defaultAK4_680.root",
        "MC_defaultAK4_635.root",
        "MC_defaultAK4_554.root",
        "MC_defaultAK4_509.root",
        "MC_defaultAK4_473.root",
        "MC_defaultAK4_428.root",
        "MC_defaultAK4_347.root",
        "MC_defaultAK4_266.root",
        "MC_defaultAK4_185.root",
        "MC_defaultAK4_717.root",
        "MC_defaultAK4_2-71.root",
        "MC_defaultAK4_2-26.root",
        "MC_defaultAK4_681.root",
        "MC_defaultAK4_636.root",
        "MC_defaultAK4_555.root",
        "MC_defaultAK4_474.root",
        "MC_defaultAK4_429.root",
        "MC_defaultAK4_348.root",
        "MC_defaultAK4_267.root",
        "MC_defaultAK4_186.root",
        "MC_defaultAK4_718.root",
        "MC_defaultAK4_2-72.root",
        "MC_defaultAK4_2-27.root",
        "MC_defaultAK4_682.root",
        "MC_defaultAK4_637.root",
        "MC_defaultAK4_556.root",
        "MC_defaultAK4_475.root",
        "MC_defaultAK4_268.root",
        "MC_defaultAK4_187.root",
        "MC_defaultAK4_719.root",
        "MC_defaultAK4_2-73.root",
        "MC_defaultAK4_2-28.root",
        "MC_defaultAK4_683.root",
        "MC_defaultAK4_638.root",
        "MC_defaultAK4_557.root",
        "MC_defaultAK4_476.root",
        "MC_defaultAK4_269.root",
        "MC_defaultAK4_188.root",
        "MC_defaultAK4_2-74.root",
        "MC_defaultAK4_2-29.root",
        "MC_defaultAK4_684.root",
        "MC_defaultAK4_639.root",
        "MC_defaultAK4_558.root",
        "MC_defaultAK4_477.root",
        "MC_defaultAK4_189.root",
        "MC_defaultAK4_2-75.root",
        "MC_defaultAK4_685.root",
        "MC_defaultAK4_559.root",
        "MC_defaultAK4_478.root",
        "MC_defaultAK4_40.root",
        "MC_defaultAK4_2-76.root",
        "MC_defaultAK4_686.root",
        "MC_defaultAK4_479.root",
        "MC_defaultAK4_41.root",
        "MC_defaultAK4_2-77.root",
        "MC_defaultAK4_687.root",
        "MC_defaultAK4_42.root",
        "MC_defaultAK4_2-78.root",
        "MC_defaultAK4_688.root",
        "MC_defaultAK4_43.root",
        "MC_defaultAK4_2-79.root",
        "MC_defaultAK4_689.root",
        "MC_defaultAK4_44.root",
        "MC_defaultAK4_90.root",
        "MC_defaultAK4_45.root",
        "MC_defaultAK4_91.root",
        "MC_defaultAK4_46.root",
        "MC_defaultAK4_92.root",
        "MC_defaultAK4_47.root",
        "MC_defaultAK4_93.root",
        "MC_defaultAK4_48.root",
        "MC_defaultAK4_94.root",
        "MC_defaultAK4_49.root",
        "MC_defaultAK4_95.root",
        "MC_defaultAK4_2-1.root",
        "MC_defaultAK4_96.root",
        "MC_defaultAK4_2-2.root",
        "MC_defaultAK4_97.root",
        "MC_defaultAK4_2-3.root",
        "MC_defaultAK4_98.root",
        "MC_defaultAK4_300.root",
        "MC_defaultAK4_2-4.root",
        "MC_defaultAK4_99.root",
        "MC_defaultAK4_301.root",
        "MC_defaultAK4_220.root",
        "MC_defaultAK4_2-5.root",
        "MC_defaultAK4_302.root",
        "MC_defaultAK4_221.root",
        "MC_defaultAK4_2-6.root",
        "MC_defaultAK4_140.root",
        "MC_defaultAK4_510.root",
        "MC_defaultAK4_303.root",
        "MC_defaultAK4_222.root",
        "MC_defaultAK4_2-7.root",
        "MC_defaultAK4_141.root",
        "MC_defaultAK4_511.root",
        "MC_defaultAK4_430.root",
        "MC_defaultAK4_304.root",
        "MC_defaultAK4_223.root",
        "MC_defaultAK4_2-8.root",
        "MC_defaultAK4_142.root",
        "MC_defaultAK4_512.root",
        "MC_defaultAK4_431.root",
        "MC_defaultAK4_350.root",
        "MC_defaultAK4_305.root",
        "MC_defaultAK4_224.root",
        "MC_defaultAK4_2-9.root",
        "MC_defaultAK4_143.root",
        "MC_defaultAK4_720.root",
        "MC_defaultAK4_513.root",
        "MC_defaultAK4_432.root",
        "MC_defaultAK4_351.root",
        "MC_defaultAK4_306.root",
        "MC_defaultAK4_270.root",
        "MC_defaultAK4_225.root",
        "MC_defaultAK4_144.root",
        "MC_defaultAK4_721.root",
        "MC_defaultAK4_2-30.root",
        "MC_defaultAK4_640.root",
        "MC_defaultAK4_514.root",
        "MC_defaultAK4_433.root",
        "MC_defaultAK4_352.root",
        "MC_defaultAK4_307.root",
        "MC_defaultAK4_271.root",
        "MC_defaultAK4_226.root",
        "MC_defaultAK4_190.root",
        "MC_defaultAK4_145.root",
        "MC_defaultAK4_722.root",
        "MC_defaultAK4_2-31.root",
        "MC_defaultAK4_641.root",
        "MC_defaultAK4_1-10.root",
        "MC_defaultAK4_560.root",
        "MC_defaultAK4_515.root",
        "MC_defaultAK4_434.root",
        "MC_defaultAK4_353.root",
        "MC_defaultAK4_308.root",
        "MC_defaultAK4_272.root",
        "MC_defaultAK4_227.root",
        "MC_defaultAK4_191.root",
        "MC_defaultAK4_146.root",
        "MC_defaultAK4_723.root",
        "MC_defaultAK4_2-32.root",
        "MC_defaultAK4_642.root",
        "MC_defaultAK4_1-11.root",
        "MC_defaultAK4_561.root",
        "MC_defaultAK4_516.root",
        "MC_defaultAK4_480.root",
        "MC_defaultAK4_435.root",
        "MC_defaultAK4_354.root",
        "MC_defaultAK4_309.root",
        "MC_defaultAK4_273.root",
        "MC_defaultAK4_228.root",
        "MC_defaultAK4_192.root",
        "MC_defaultAK4_147.root",
        "MC_defaultAK4_2-33.root",
        "MC_defaultAK4_643.root",
        "MC_defaultAK4_1-12.root",
        "MC_defaultAK4_562.root",
        "MC_defaultAK4_517.root",
        "MC_defaultAK4_481.root",
        "MC_defaultAK4_355.root",
        "MC_defaultAK4_274.root",
        "MC_defaultAK4_229.root",
        "MC_defaultAK4_193.root",
        "MC_defaultAK4_148.root",
        "MC_defaultAK4_725.root",
        "MC_defaultAK4_2-34.root",
        "MC_defaultAK4_644.root",
        "MC_defaultAK4_1-13.root",
        "MC_defaultAK4_563.root",
        "MC_defaultAK4_518.root",
        "MC_defaultAK4_482.root",
        "MC_defaultAK4_437.root",
        "MC_defaultAK4_356.root",
        "MC_defaultAK4_275.root",
        "MC_defaultAK4_194.root",
        "MC_defaultAK4_149.root",
        "MC_defaultAK4_726.root",
        "MC_defaultAK4_2-80.root",
        "MC_defaultAK4_2-35.root",
        "MC_defaultAK4_690.root",
        "MC_defaultAK4_645.root",
        "MC_defaultAK4_1-14.root",
        "MC_defaultAK4_564.root",
        "MC_defaultAK4_519.root",
        "MC_defaultAK4_483.root",
        "MC_defaultAK4_357.root",
        "MC_defaultAK4_276.root",
        "MC_defaultAK4_195.root",
        "MC_defaultAK4_727.root",
        "MC_defaultAK4_2-81.root",
        "MC_defaultAK4_2-36.root",
        "MC_defaultAK4_691.root",
        "MC_defaultAK4_646.root",
        "MC_defaultAK4_1-15.root",
        "MC_defaultAK4_565.root",
        "MC_defaultAK4_484.root",
        "MC_defaultAK4_439.root",
        "MC_defaultAK4_358.root",
        "MC_defaultAK4_277.root",
        "MC_defaultAK4_196.root",
        "MC_defaultAK4_728.root",
        "MC_defaultAK4_2-82.root",
        "MC_defaultAK4_2-37.root",
        "MC_defaultAK4_692.root",
        "MC_defaultAK4_647.root",
        "MC_defaultAK4_1-16.root",
        "MC_defaultAK4_566.root",
        "MC_defaultAK4_485.root",
        "MC_defaultAK4_359.root",
        "MC_defaultAK4_278.root",
        "MC_defaultAK4_197.root",
        "MC_defaultAK4_729.root",
        "MC_defaultAK4_2-83.root",
        "MC_defaultAK4_2-38.root",
        "MC_defaultAK4_693.root",
        "MC_defaultAK4_648.root",
        "MC_defaultAK4_1-17.root",
        "MC_defaultAK4_567.root",
        "MC_defaultAK4_486.root",
        "MC_defaultAK4_279.root",
        "MC_defaultAK4_198.root",
        "MC_defaultAK4_2-84.root",
        "MC_defaultAK4_2-39.root",
        "MC_defaultAK4_694.root",
        "MC_defaultAK4_649.root",
        "MC_defaultAK4_1-18.root",
        "MC_defaultAK4_568.root",
        "MC_defaultAK4_487.root",
        "MC_defaultAK4_199.root",
        "MC_defaultAK4_2-85.root",
        "MC_defaultAK4_695.root",
        "MC_defaultAK4_1-19.root",
        "MC_defaultAK4_569.root",
        "MC_defaultAK4_488.root",
        "MC_defaultAK4_50.root",
        "MC_defaultAK4_2-86.root",
        "MC_defaultAK4_696.root",
        "MC_defaultAK4_489.root",
        "MC_defaultAK4_51.root",
        "MC_defaultAK4_697.root",
        "MC_defaultAK4_52.root",
        "MC_defaultAK4_698.root",
        "MC_defaultAK4_53.root",
        "MC_defaultAK4_699.root",
        "MC_defaultAK4_54.root",
        "MC_defaultAK4_55.root",
        "MC_defaultAK4_56.root",
        "MC_defaultAK4_57.root",
        "MC_defaultAK4_58.root",
        "MC_defaultAK4_59.root",
        "MC_defaultAK4_100.root",
    ),
)