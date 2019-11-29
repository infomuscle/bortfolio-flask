getWork = """
        SELECT
                    WORK_NO
                  , TITLE
                  , SUB_TITLE
                  , CTG
                  , DESCRIPTION
                  , CLIENT
                  , DATE_FORMAT(STRT_DT, '%M %Y') AS STRT_DT
                  , DATE_FORMAT(END_DT, '%M %Y') AS END_DT
                  , REP_IMG
                  , URL
                  , USE_YN
        FROM        WORK
        WHERE       1 = 1
        AND         USE_YN = 'Y'
        ORDER BY    WORK_NO
        ;
        """

getExperience = """
        SELECT
                COMPANY
              , JOB
              , DESCRIPTION
              , DATE_FORMAT(STRT_DT, '%M %Y') AS STRT_DT
              , DATE_FORMAT(END_DT, '%M %Y') AS END_DT
        FROM    EXPERIENCE
        WHERE       1 = 1
        AND         USE_YN = 'Y'
        ORDER BY    EXP_NO DESC
        ;
        """

getEducation = """
        SELECT
                SCHOOL
              , DEGREE
              , STUDY
              , GRADE
              , GRADE_MAX
              , DATE_FORMAT(STRT_DT, '%M %Y') AS STRT_DT
              , DATE_FORMAT(END_DT, '%M %Y') AS END_DT
        FROM    EDUCATION
        WHERE   1 = 1
        ORDER BY EDU_NO DESC
        ;
        """

getSkillLanguage = """
        SELECT      *
        FROM        SKILL
        WHERE       1 = 1
        AND         SKILL_TYPE = 'Language'
        # AND         USE_PERIOD IS NOT NULL
        # AND         LOGO_IMG IS NOT NULL
        AND         USE_YN = 'Y'
        ORDER BY    SKILL_NO
        ;
        """

getSkillFramework = """
        SELECT      *
        FROM        SKILL
        WHERE       1 = 1
        AND         SKILL_TYPE = 'Framework'
        # AND         USE_PERIOD IS NOT NULL
        # AND         LOGO_IMG IS NOT NULL
        AND         USE_YN = 'Y'
        ORDER BY    SKILL_NO
        ;
        """

getCert = """
        SELECT
                    CERT_NM
                  , DESCRIPTION
                  , ISSUER
                  , DATE_FORMAT(ISSUE_DT, '%M %Y') AS ISSUE_DT
        FROM        CERTIFICATION
        WHERE       1 = 1
        AND         USE_YN = 'Y'
        ORDER BY    CERT_NO
        ;
        """



### ADMIN 테이블 컨트롤 ###
getColumns = """
        SELECT      COLUMN_NAME
        FROM        INFORMATION_SCHEMA.COLUMNS
        WHERE       1 = 1    
        AND         TABLE_SCHEMA='BORTFOLIO_FLASK'
        AND         TABLE_NAME='{table}'
        ORDER BY    ORDINAL_POSITION
        ;
        """

getTable = """
        SELECT      *
        FROM        {table}
        WHERE       1 = 1
        ORDER BY    {order}
        ;
        """

insertData = """
        INSERT INTO {table}
        VALUES      {values}
        ;
        """

updateData = """
        UPDATE  {table}
        SET     {setting}
        WHERE   {pkColumn} = '{pkValue}'       
        ;
        
        """

deleteData = """
        DELETE FROM {table}
        WHERE  {pkColumn} = '{pkValue}'
        ;
        """
