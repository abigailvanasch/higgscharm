from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="MuonD",
    process="Data",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "data_2022_MINIAODv4/Muon/Run2022D-22Sep2023-v1_BTV_Run3_2022_Comm_MINIAODv4/240429_092058/0000/"
    ),
    key="Events",
    year="2022",
    era="D",
    xsec=None,
    partitions=15,
    stepsize=50_000,
    filenames=(
        "data_defaultAK4_2023_181.root",
        "data_defaultAK4_2023_214.root",
        "data_defaultAK4_2023_13.root",
        "data_defaultAK4_2023_16.root",
        "data_defaultAK4_2023_18.root",
        "data_defaultAK4_2023_15.root",
        "data_defaultAK4_2023_10.root",
        "data_defaultAK4_2023_180.root",
        "data_defaultAK4_2023_182.root",
        "data_defaultAK4_2023_11.root",
        "data_defaultAK4_2023_14.root",
        "data_defaultAK4_2023_17.root",
        "data_defaultAK4_2023_183.root",
        "data_defaultAK4_2023_213.root",
        "data_defaultAK4_2023_185.root",
        "data_defaultAK4_2023_28.root",
        "data_defaultAK4_2023_19.root",
        "data_defaultAK4_2023_20.root",
        "data_defaultAK4_2023_184.root",
        "data_defaultAK4_2023_12.root",
        "data_defaultAK4_2023_74.root",
        "data_defaultAK4_2023_26.root",
        "data_defaultAK4_2023_29.root",
        "data_defaultAK4_2023_57.root",
        "data_defaultAK4_2023_61.root",
        "data_defaultAK4_2023_24.root",
        "data_defaultAK4_2023_59.root",
        "data_defaultAK4_2023_58.root",
        "data_defaultAK4_2023_27.root",
        "data_defaultAK4_2023_191.root",
        "data_defaultAK4_2023_63.root",
        "data_defaultAK4_2023_51.root",
        "data_defaultAK4_2023_196.root",
        "data_defaultAK4_2023_211.root",
        "data_defaultAK4_2023_21.root",
        "data_defaultAK4_2023_62.root",
        "data_defaultAK4_2023_56.root",
        "data_defaultAK4_2023_55.root",
        "data_defaultAK4_2023_50.root",
        "data_defaultAK4_2023_189.root",
        "data_defaultAK4_2023_187.root",
        "data_defaultAK4_2023_65.root",
        "data_defaultAK4_2023_188.root",
        "data_defaultAK4_2023_22.root",
        "data_defaultAK4_2023_192.root",
        "data_defaultAK4_2023_193.root",
        "data_defaultAK4_2023_199.root",
        "data_defaultAK4_2023_66.root",
        "data_defaultAK4_2023_100.root",
        "data_defaultAK4_2023_52.root",
        "data_defaultAK4_2023_75.root",
        "data_defaultAK4_2023_198.root",
        "data_defaultAK4_2023_60.root",
        "data_defaultAK4_2023_71.root",
        "data_defaultAK4_2023_76.root",
        "data_defaultAK4_2023_194.root",
        "data_defaultAK4_2023_69.root",
        "data_defaultAK4_2023_77.root",
        "data_defaultAK4_2023_70.root",
        "data_defaultAK4_2023_212.root",
        "data_defaultAK4_2023_210.root",
        "data_defaultAK4_2023_73.root",
        "data_defaultAK4_2023_68.root",
        "data_defaultAK4_2023_102.root",
        "data_defaultAK4_2023_54.root",
        "data_defaultAK4_2023_72.root",
        "data_defaultAK4_2023_186.root",
        "data_defaultAK4_2023_190.root",
        "data_defaultAK4_2023_53.root",
        "data_defaultAK4_2023_103.root",
        "data_defaultAK4_2023_25.root",
        "data_defaultAK4_2023_101.root",
        "data_defaultAK4_2023_105.root",
        "data_defaultAK4_2023_104.root",
        "data_defaultAK4_2023_220.root",
        "data_defaultAK4_2023_23.root",
        "data_defaultAK4_2023_219.root",
        "data_defaultAK4_2023_215.root",
        "data_defaultAK4_2023_195.root",
        "data_defaultAK4_2023_106.root",
        "data_defaultAK4_2023_217.root",
        "data_defaultAK4_2023_222.root",
        "data_defaultAK4_2023_64.root",
        "data_defaultAK4_2023_134.root",
        "data_defaultAK4_2023_132.root",
        "data_defaultAK4_2023_133.root",
        "data_defaultAK4_2023_130.root",
        "data_defaultAK4_2023_139.root",
        "data_defaultAK4_2023_151.root",
        "data_defaultAK4_2023_150.root",
        "data_defaultAK4_2023_67.root",
        "data_defaultAK4_2023_138.root",
        "data_defaultAK4_2023_131.root",
        "data_defaultAK4_2023_143.root",
        "data_defaultAK4_2023_141.root",
        "data_defaultAK4_2023_149.root",
        "data_defaultAK4_2023_137.root",
        "data_defaultAK4_2023_148.root",
        "data_defaultAK4_2023_136.root",
        "data_defaultAK4_2023_144.root",
        "data_defaultAK4_2023_145.root",
        "data_defaultAK4_2023_147.root",
        "data_defaultAK4_2023_140.root",
        "data_defaultAK4_2023_146.root",
        "data_defaultAK4_2023_225.root",
        "data_defaultAK4_2023_142.root",
        "data_defaultAK4_2023_218.root",
        "data_defaultAK4_2023_216.root",
        "data_defaultAK4_2023_221.root",
        "data_defaultAK4_2023_223.root",
        "data_defaultAK4_2023_224.root",
        "data_defaultAK4_2023_78.root",
        "data_defaultAK4_2023_152.root",
        "data_defaultAK4_2023_107.root",
        "data_defaultAK4_2023_79.root",
        "data_defaultAK4_2023_153.root",
        "data_defaultAK4_2023_108.root",
        "data_defaultAK4_2023_154.root",
        "data_defaultAK4_2023_155.root",
        "data_defaultAK4_2023_156.root",
        "data_defaultAK4_2023_157.root",
        "data_defaultAK4_2023_158.root",
        "data_defaultAK4_2023_159.root",
        "data_defaultAK4_2023_1.root",
        "data_defaultAK4_2023_30.root",
        "data_defaultAK4_2023_2.root",
        "data_defaultAK4_2023_31.root",
        "data_defaultAK4_2023_3.root",
        "data_defaultAK4_2023_32.root",
        "data_defaultAK4_2023_4.root",
        "data_defaultAK4_2023_33.root",
        "data_defaultAK4_2023_5.root",
        "data_defaultAK4_2023_34.root",
        "data_defaultAK4_2023_6.root",
        "data_defaultAK4_2023_80.root",
        "data_defaultAK4_2023_35.root",
        "data_defaultAK4_2023_7.root",
        "data_defaultAK4_2023_81.root",
        "data_defaultAK4_2023_36.root",
        "data_defaultAK4_2023_110.root",
        "data_defaultAK4_2023_8.root",
        "data_defaultAK4_2023_82.root",
        "data_defaultAK4_2023_37.root",
        "data_defaultAK4_2023_111.root",
        "data_defaultAK4_2023_9.root",
        "data_defaultAK4_2023_83.root",
        "data_defaultAK4_2023_38.root",
        "data_defaultAK4_2023_112.root",
        "data_defaultAK4_2023_84.root",
        "data_defaultAK4_2023_39.root",
        "data_defaultAK4_2023_113.root",
        "data_defaultAK4_2023_85.root",
        "data_defaultAK4_2023_114.root",
        "data_defaultAK4_2023_86.root",
        "data_defaultAK4_2023_160.root",
        "data_defaultAK4_2023_115.root",
        "data_defaultAK4_2023_87.root",
        "data_defaultAK4_2023_161.root",
        "data_defaultAK4_2023_116.root",
        "data_defaultAK4_2023_88.root",
        "data_defaultAK4_2023_162.root",
        "data_defaultAK4_2023_117.root",
        "data_defaultAK4_2023_89.root",
        "data_defaultAK4_2023_163.root",
        "data_defaultAK4_2023_118.root",
        "data_defaultAK4_2023_164.root",
        "data_defaultAK4_2023_119.root",
        "data_defaultAK4_2023_165.root",
        "data_defaultAK4_2023_166.root",
        "data_defaultAK4_2023_167.root",
        "data_defaultAK4_2023_168.root",
        "data_defaultAK4_2023_169.root",
        "data_defaultAK4_2023_40.root",
        "data_defaultAK4_2023_41.root",
        "data_defaultAK4_2023_42.root",
        "data_defaultAK4_2023_43.root",
        "data_defaultAK4_2023_44.root",
        "data_defaultAK4_2023_90.root",
        "data_defaultAK4_2023_45.root",
        "data_defaultAK4_2023_200.root",
        "data_defaultAK4_2023_91.root",
        "data_defaultAK4_2023_46.root",
        "data_defaultAK4_2023_201.root",
        "data_defaultAK4_2023_120.root",
        "data_defaultAK4_2023_92.root",
        "data_defaultAK4_2023_47.root",
        "data_defaultAK4_2023_202.root",
        "data_defaultAK4_2023_121.root",
        "data_defaultAK4_2023_93.root",
        "data_defaultAK4_2023_48.root",
        "data_defaultAK4_2023_203.root",
        "data_defaultAK4_2023_122.root",
        "data_defaultAK4_2023_94.root",
        "data_defaultAK4_2023_49.root",
        "data_defaultAK4_2023_204.root",
        "data_defaultAK4_2023_123.root",
        "data_defaultAK4_2023_95.root",
        "data_defaultAK4_2023_205.root",
        "data_defaultAK4_2023_124.root",
        "data_defaultAK4_2023_96.root",
        "data_defaultAK4_2023_206.root",
        "data_defaultAK4_2023_170.root",
        "data_defaultAK4_2023_125.root",
        "data_defaultAK4_2023_97.root",
        "data_defaultAK4_2023_207.root",
        "data_defaultAK4_2023_126.root",
        "data_defaultAK4_2023_98.root",
        "data_defaultAK4_2023_208.root",
        "data_defaultAK4_2023_172.root",
        "data_defaultAK4_2023_127.root",
        "data_defaultAK4_2023_99.root",
        "data_defaultAK4_2023_209.root",
        "data_defaultAK4_2023_173.root",
        "data_defaultAK4_2023_128.root",
        "data_defaultAK4_2023_174.root",
        "data_defaultAK4_2023_129.root",
        "data_defaultAK4_2023_175.root",
        "data_defaultAK4_2023_176.root",
        "data_defaultAK4_2023_177.root",
        "data_defaultAK4_2023_179.root",
    ),
)