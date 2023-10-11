job_types = {
    "JT00": "All Jobs",
    "JT01": "Primary Jobs",
    "JT02": "All Private Jobs",
    "JT03": "Private Primary Jobs",
    "JT04": "All Federal Jobs",
    "JT05": "Federal Primary Jobs",
}
workforce_types = {
    "S000": "Total number of jobs,",
    "SA01": "Number of jobs of workers age 29 or younger",
    "SA02": "Number of jobs for workers age 30 to 54",
    "SA03": "Number of jobs for workers age 55 or older",
    "SE01": "Number of jobs with earnings $1250/month or less",
    "SE02": "Number of jobs with earnings $1251/month to $3333/month",
    "SE03": "Number of jobs with earnings greater than $3333/month",
    "SI01": "Number of jobs in Goods Producing industry sectors",
    "SI02": "Number of jobs in Trade, Transportation, and Utilities industry sectors",
    "SI03": "Number of jobs in All Other Services industry sectors",
}

od_table = """
    w_geocode char(15) not null,
    h_geocode char(15) not null,
    s000 int,
    sa01 int,
    sa02 int,
    sa03 int,
    se01 int,
    se02 int,
    se03 int,
    si01 int,
    si02 int,
    si03 int,
    createdate char(8),
    job_type char(4),
    state char(2),
    dvrpc_reg bool,
    scope varchar
    """

od_temp_table = """
    SELECT
        w_geocode,
        h_geocode,
        s000,
        sa01,
        sa02,
        sa03,
        se01,
        se02,
        se03,
        si01,
        si02,
        si03,
        createdate
    FROM od.combined_od_table WITH NO DATA;

"""

wac_table = """
    w_geocode char(15),
    C000 numeric,
    CA01 numeric,
    CA02 numeric,
    CA03 numeric,
    CE01 numeric,
    CE02 numeric,
    CE03 numeric,
    CNS01 numeric,
    CNS02 numeric,
    CNS03 numeric,
    CNS04 numeric,
    CNS05 numeric,
    CNS06 numeric,
    CNS07 numeric,
    CNS08 numeric,
    CNS09 numeric,
    CNS10 numeric,
    CNS11 numeric,
    CNS12 numeric,
    CNS13 numeric,
    CNS14 numeric,
    CNS15 numeric,
    CNS16 numeric,
    CNS17 numeric,
    CNS18 numeric,
    CNS19 numeric,
    CNS20 numeric,
    CR01 numeric,
    CR02 numeric,
    CR03 numeric,
    CR04 numeric,
    CR05 numeric,
    CR07 numeric,
    CT01 numeric,
    CT02 numeric,
    CD01 numeric,
    CD02 numeric,
    CD03 numeric,
    CD04 numeric,
    CS01 numeric,
    CS02 numeric,
    CFA01 numeric,
    CFA02 numeric,
    CFA03 numeric,
    CFA04 numeric,
    CFA05 numeric,
    CFS01 numeric,
    CFS02 numeric,
    CFS03 numeric,
    CFS04 numeric,
    CFS05 numeric,
    createdate char(8),
    state char(2),
    job_type char(4),
    segment char(4),
    dvrpc_reg bool 

    """


wac_temp_table = """
      select 
        w_geocode,
        C000,
        CA01,
        CA02,
        CA03,
        CE01,
        CE02,
        CE03,
        CNS01,
        CNS02,
        CNS03,
        CNS04,
        CNS05,
        CNS06,
        CNS07,
        CNS08,
        CNS09,
        CNS10,
        CNS11,
        CNS12,
        CNS13,
        CNS14,
        CNS15,
        CNS16,
        CNS17,
        CNS18,
        CNS19,
        CNS20,
        CR01,
        CR02,
        CR03,
        CR04,
        CR05,
        CR07,
        CT01,
        CT02,
        CD01,
        CD02,
        CD03,
        CD04,
        CS01,
        CS02,
        CFA01,
        CFA02,
        CFA03,
        CFA04,
        CFA05,
        CFS01,
        CFS02,
        CFS03,
        CFS04,
        CFS05,
        createdate
    FROM wac.combined_wac_table
    WITH NO DATA;

"""


rac_table = """
    h_geocode char(15),
    C000 numeric,
    CA01 numeric,
    CA02 numeric,
    CA03 numeric,
    CE01 numeric,
    CE02 numeric,
    CE03 numeric,
    CNS01 numeric,
    CNS02 numeric,
    CNS03 numeric,
    CNS04 numeric,
    CNS05 numeric,
    CNS06 numeric,
    CNS07 numeric,
    CNS08 numeric,
    CNS09 numeric,
    CNS10 numeric,
    CNS11 numeric,
    CNS12 numeric,
    CNS13 numeric,
    CNS14 numeric,
    CNS15 numeric,
    CNS16 numeric,
    CNS17 numeric,
    CNS18 numeric,
    CNS19 numeric,
    CNS20 numeric,
    CR01 numeric,
    CR02 numeric,
    CR03 numeric,
    CR04 numeric,
    CR05 numeric,
    CR07 numeric,
    CT01 numeric,
    CT02 numeric,
    CD01 numeric,
    CD02 numeric,
    CD03 numeric,
    CD04 numeric,
    CS01 numeric,
    CS02 numeric,
    createdate CHAR(8),
    state char(2),
    job_type char(4),
    segment char(4),
    dvrpc_reg bool
"""

rac_temp_table = """
    
  select 
    h_geocode,
    C000,
    CA01,
    CA02,
    CA03,
    CE01,
    CE02,
    CE03,
    CNS01,
    CNS02,
    CNS03,
    CNS04,
    CNS05,
    CNS06,
    CNS07,
    CNS08,
    CNS09,
    CNS10,
    CNS11,
    CNS12,
    CNS13,
    CNS14,
    CNS15,
    CNS16,
    CNS17,
    CNS18,
    CNS19,
    CNS20,
    CR01,
    CR02,
    CR03,
    CR04,
    CR05,
    CR07,
    CT01,
    CT02,
    CD01,
    CD02,
    CD03,
    CD04,
    CS01,
    CS02,
    createdate 
    FROM rac.combined_rac_table
    WITH NO DATA;
"""

xwalk = """
    tabblk2020 char(15) not null,
    st char(2), 
    st_usps char(2),
    stname char(100),
    cty char(5),
    ctyname char(100),
    trct char(11),
    trctname char(100),
    bgrp char(12),
    bgrpname char(100),
    cbsa char(5),
    cbsaname char(100),
    zcta char(5),
    zctaname char(100),
    stplc char(7),
    stplcname char(100),
    ctycsub char(10),
    ctycsubname char(100),
    stcd116 char(4),
    stcd116name char(100),
    stsldl char(5),
    stsldlname char(100),
    stsldu char(5), 
    stslduname char(100),
    stschool char(7),
    stschoolname char(100),
    stsecon char(7),
    stseconname char(100),
    trib char(5),
    tribname char(100),
    tsub char(7),
    tsubname char(100),
    stanrc char(7), 
    stanrcname char(100),
    necta char(5),
    nectaname char(100),
    mil char(22),
    milname char(100), 
    stwib char(8),
    stwibname char(100),
    blklatdd numeric,
    blklondd numeric,
    createdate char(8)
    """


xwalk_temp_table = """
    SELECT *
    FROM geo_xwalk.xwalk WITH NO DATA;

"""

dvrpc_counties = [
    'Bucks County, PA',
    'Chester County, PA',
    'Delaware County, PA',
    'Montgomery County, PA',
    'Philadelphia County, PA',
    'Burlington County, NJ',
    'Camden County, NJ',
    'Gloucester County, NJ',
    'Mercer County, NJ',
]
