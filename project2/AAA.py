# noinspection PyUnresolvedReferences
import zid_project2 as prj2
# noinspection PyUnresolvedReferences
import config as cfg


tickers=cfg.TICKERS

prc_df=prj2.mk_prc_df(tickers,prc_col='adj_close')
#print(prc_df)
ret_df=prj2.mk_ret_df(prc_df)
#print(ret_df)
aret_df=prj2.mk_aret_df(ret_df)
#print(aret_df)

print(prj2.get_avg(ret_df,'AAL',2020))