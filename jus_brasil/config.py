from starlette.config import Config


config = Config('../.env')

TJSP_PG = config("TJSP_PG", default="https://esaj.tjsp.jus.br/cpopg/search.do")
TJSP_SG = config("TJSP_SG", default="https://esaj.tjsp.jus.br/cposg/search.do")
TJSP_SG_REC = config("TJSP_SG_REC", default="https://esaj.tjsp.jus.br/cposgcr/search.do")

TJMS_PG = config("TJMS_PG", default="https://esaj.tjms.jus.br/cpopg5/search.do")
TJMS_SG = config("TJMS_SG", default="https://esaj.tjms.jus.br/cposg5/search.do")
