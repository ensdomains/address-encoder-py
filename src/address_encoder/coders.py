from __future__ import annotations

from address_encoder.coins.abbc import decode_abbc_address, encode_abbc_address
from address_encoder.coins.ada import decode_ada_address, encode_ada_address
from address_encoder.coins.ae import decode_ae_address, encode_ae_address
from address_encoder.coins.aib import decode_aib_address, encode_aib_address
from address_encoder.coins.aion import decode_aion_address, encode_aion_address
from address_encoder.coins.algo import decode_algo_address, encode_algo_address
from address_encoder.coins.ar import decode_ar_address, encode_ar_address
from address_encoder.coins.ardr import decode_ardr_address, encode_ardr_address
from address_encoder.coins.ark import decode_ark_address, encode_ark_address
from address_encoder.coins.atom import decode_atom_address, encode_atom_address
from address_encoder.coins.avax import decode_avax_address, encode_avax_address
from address_encoder.coins.bcd import decode_bcd_address, encode_bcd_address
from address_encoder.coins.bch import decode_bch_address, encode_bch_address
from address_encoder.coins.bcn import decode_bcn_address, encode_bcn_address
from address_encoder.coins.bdx import decode_bdx_address, encode_bdx_address
from address_encoder.coins.bnb import decode_bnb_address, encode_bnb_address
from address_encoder.coins.bps import decode_bps_address, encode_bps_address
from address_encoder.coins.bsv import decode_bsv_address, encode_bsv_address
from address_encoder.coins.btc import decode_btc_address, encode_btc_address
from address_encoder.coins.btg import decode_btg_address, encode_btg_address
from address_encoder.coins.btm import decode_btm_address, encode_btm_address
from address_encoder.coins.bts import decode_bts_address, encode_bts_address
from address_encoder.coins.cca import decode_cca_address, encode_cca_address
from address_encoder.coins.ccxx import decode_ccxx_address, encode_ccxx_address
from address_encoder.coins.celoLegacy import decode_celoLegacy_address, encode_celoLegacy_address
from address_encoder.coins.ckb import decode_ckb_address, encode_ckb_address
from address_encoder.coins.cloLegacy import decode_cloLegacy_address, encode_cloLegacy_address
from address_encoder.coins.dash import decode_dash_address, encode_dash_address
from address_encoder.coins.dcr import decode_dcr_address, encode_dcr_address
from address_encoder.coins.dgb import decode_dgb_address, encode_dgb_address
from address_encoder.coins.divi import decode_divi_address, encode_divi_address
from address_encoder.coins.doge import decode_doge_address, encode_doge_address
from address_encoder.coins.dot import decode_dot_address, encode_dot_address
from address_encoder.coins.egld import decode_egld_address, encode_egld_address
from address_encoder.coins.ela import decode_ela_address, encode_ela_address
from address_encoder.coins.eos import decode_eos_address, encode_eos_address
from address_encoder.coins.etcLegacy import decode_etcLegacy_address, encode_etcLegacy_address
from address_encoder.coins.eth import decode_eth_address, encode_eth_address
from address_encoder.coins.etn import decode_etn_address, encode_etn_address
from address_encoder.coins.ewtLegacy import decode_ewtLegacy_address, encode_ewtLegacy_address
from address_encoder.coins.fil import decode_fil_address, encode_fil_address
from address_encoder.coins.fio import decode_fio_address, encode_fio_address
from address_encoder.coins.firo import decode_firo_address, encode_firo_address
from address_encoder.coins.flow import decode_flow_address, encode_flow_address
from address_encoder.coins.flux import decode_flux_address, encode_flux_address
from address_encoder.coins.ftmLegacy import decode_ftmLegacy_address, encode_ftmLegacy_address
from address_encoder.coins.gnoLegacy import decode_gnoLegacy_address, encode_gnoLegacy_address
from address_encoder.coins.goLegacy import decode_goLegacy_address, encode_goLegacy_address
from address_encoder.coins.grin import decode_grin_address, encode_grin_address
from address_encoder.coins.gxc import decode_gxc_address, encode_gxc_address
from address_encoder.coins.hbar import decode_hbar_address, encode_hbar_address
from address_encoder.coins.hive import decode_hive_address, encode_hive_address
from address_encoder.coins.hns import decode_hns_address, encode_hns_address
from address_encoder.coins.hnt import decode_hnt_address, encode_hnt_address
from address_encoder.coins.icx import decode_icx_address, encode_icx_address
from address_encoder.coins.iost import decode_iost_address, encode_iost_address
from address_encoder.coins.iota import decode_iota_address, encode_iota_address
from address_encoder.coins.iotx import decode_iotx_address, encode_iotx_address
from address_encoder.coins.iris import decode_iris_address, encode_iris_address
from address_encoder.coins.kava import decode_kava_address, encode_kava_address
from address_encoder.coins.kmd import decode_kmd_address, encode_kmd_address
from address_encoder.coins.ksm import decode_ksm_address, encode_ksm_address
from address_encoder.coins.lcc import decode_lcc_address, encode_lcc_address
from address_encoder.coins.lrg import decode_lrg_address, encode_lrg_address
from address_encoder.coins.lsk import decode_lsk_address, encode_lsk_address
from address_encoder.coins.ltc import decode_ltc_address, encode_ltc_address
from address_encoder.coins.luna import decode_luna_address, encode_luna_address
from address_encoder.coins.mona import decode_mona_address, encode_mona_address
from address_encoder.coins.mrx import decode_mrx_address, encode_mrx_address
from address_encoder.coins.nano import decode_nano_address, encode_nano_address
from address_encoder.coins.nas import decode_nas_address, encode_nas_address
from address_encoder.coins.near import decode_near_address, encode_near_address
from address_encoder.coins.neo import decode_neo_address, encode_neo_address
from address_encoder.coins.nim import decode_nim_address, encode_nim_address
from address_encoder.coins.nmc import decode_nmc_address, encode_nmc_address
from address_encoder.coins.nostr import decode_nostr_address, encode_nostr_address
from address_encoder.coins.nrgLegacy import decode_nrgLegacy_address, encode_nrgLegacy_address
from address_encoder.coins.nuls import decode_nuls_address, encode_nuls_address
from address_encoder.coins.one import decode_one_address, encode_one_address
from address_encoder.coins.ont import decode_ont_address, encode_ont_address
from address_encoder.coins.poaLegacy import decode_poaLegacy_address, encode_poaLegacy_address
from address_encoder.coins.ppc import decode_ppc_address, encode_ppc_address
from address_encoder.coins.qtum import decode_qtum_address, encode_qtum_address
from address_encoder.coins.rbtc import decode_rbtc_address, encode_rbtc_address
from address_encoder.coins.rdd import decode_rdd_address, encode_rdd_address
from address_encoder.coins.rune import decode_rune_address, encode_rune_address
from address_encoder.coins.rvn import decode_rvn_address, encode_rvn_address
from address_encoder.coins.sc import decode_sc_address, encode_sc_address
from address_encoder.coins.sero import decode_sero_address, encode_sero_address
from address_encoder.coins.sol import decode_sol_address, encode_sol_address
from address_encoder.coins.srm import decode_srm_address, encode_srm_address
from address_encoder.coins.steem import decode_steem_address, encode_steem_address
from address_encoder.coins.strat import decode_strat_address, encode_strat_address
from address_encoder.coins.strk import decode_strk_address, encode_strk_address
from address_encoder.coins.stx import decode_stx_address, encode_stx_address
from address_encoder.coins.sui import decode_sui_address, encode_sui_address
from address_encoder.coins.sys import decode_sys_address, encode_sys_address
from address_encoder.coins.tfuel import decode_tfuel_address, encode_tfuel_address
from address_encoder.coins.thetaLegacy import decode_thetaLegacy_address, encode_thetaLegacy_address
from address_encoder.coins.tomoLegacy import decode_tomoLegacy_address, encode_tomoLegacy_address
from address_encoder.coins.trx import decode_trx_address, encode_trx_address
from address_encoder.coins.ttLegacy import decode_ttLegacy_address, encode_ttLegacy_address
from address_encoder.coins.vet import decode_vet_address, encode_vet_address
from address_encoder.coins.via import decode_via_address, encode_via_address
from address_encoder.coins.vlx import decode_vlx_address, encode_vlx_address
from address_encoder.coins.vlxLegacy import decode_vlxLegacy_address, encode_vlxLegacy_address
from address_encoder.coins.vsys import decode_vsys_address, encode_vsys_address
from address_encoder.coins.wan import decode_wan_address, encode_wan_address
from address_encoder.coins.waves import decode_waves_address, encode_waves_address
from address_encoder.coins.wicc import decode_wicc_address, encode_wicc_address
from address_encoder.coins.xch import decode_xch_address, encode_xch_address
from address_encoder.coins.xem import decode_xem_address, encode_xem_address
from address_encoder.coins.xhv import decode_xhv_address, encode_xhv_address
from address_encoder.coins.xlm import decode_xlm_address, encode_xlm_address
from address_encoder.coins.xmr import decode_xmr_address, encode_xmr_address
from address_encoder.coins.xrp import decode_xrp_address, encode_xrp_address
from address_encoder.coins.xtz import decode_xtz_address, encode_xtz_address
from address_encoder.coins.xvg import decode_xvg_address, encode_xvg_address
from address_encoder.coins.zec import decode_zec_address, encode_zec_address
from address_encoder.coins.zen import decode_zen_address, encode_zen_address
from address_encoder.coins.zil import decode_zil_address, encode_zil_address

__all__ = [
    "decode_abbc_address",
    "encode_abbc_address",
    "decode_ada_address",
    "encode_ada_address",
    "decode_ae_address",
    "encode_ae_address",
    "decode_aib_address",
    "encode_aib_address",
    "decode_aion_address",
    "encode_aion_address",
    "decode_algo_address",
    "encode_algo_address",
    "decode_ar_address",
    "encode_ar_address",
    "decode_ardr_address",
    "encode_ardr_address",
    "decode_ark_address",
    "encode_ark_address",
    "decode_atom_address",
    "encode_atom_address",
    "decode_avax_address",
    "encode_avax_address",
    "decode_bcd_address",
    "encode_bcd_address",
    "decode_bch_address",
    "encode_bch_address",
    "decode_bcn_address",
    "encode_bcn_address",
    "decode_bdx_address",
    "encode_bdx_address",
    "decode_bnb_address",
    "encode_bnb_address",
    "decode_bps_address",
    "encode_bps_address",
    "decode_bsv_address",
    "encode_bsv_address",
    "decode_btc_address",
    "encode_btc_address",
    "decode_btg_address",
    "encode_btg_address",
    "decode_btm_address",
    "encode_btm_address",
    "decode_bts_address",
    "encode_bts_address",
    "decode_cca_address",
    "encode_cca_address",
    "decode_ccxx_address",
    "encode_ccxx_address",
    "decode_celoLegacy_address",
    "encode_celoLegacy_address",
    "decode_ckb_address",
    "encode_ckb_address",
    "decode_cloLegacy_address",
    "encode_cloLegacy_address",
    "decode_dash_address",
    "encode_dash_address",
    "decode_dcr_address",
    "encode_dcr_address",
    "decode_dgb_address",
    "encode_dgb_address",
    "decode_divi_address",
    "encode_divi_address",
    "decode_doge_address",
    "encode_doge_address",
    "decode_dot_address",
    "encode_dot_address",
    "decode_egld_address",
    "encode_egld_address",
    "decode_ela_address",
    "encode_ela_address",
    "decode_eos_address",
    "encode_eos_address",
    "decode_etcLegacy_address",
    "encode_etcLegacy_address",
    "decode_eth_address",
    "encode_eth_address",
    "decode_etn_address",
    "encode_etn_address",
    "decode_ewtLegacy_address",
    "encode_ewtLegacy_address",
    "decode_fil_address",
    "encode_fil_address",
    "decode_fio_address",
    "encode_fio_address",
    "decode_firo_address",
    "encode_firo_address",
    "decode_flow_address",
    "encode_flow_address",
    "decode_flux_address",
    "encode_flux_address",
    "decode_ftmLegacy_address",
    "encode_ftmLegacy_address",
    "decode_gnoLegacy_address",
    "encode_gnoLegacy_address",
    "decode_goLegacy_address",
    "encode_goLegacy_address",
    "decode_grin_address",
    "encode_grin_address",
    "decode_gxc_address",
    "encode_gxc_address",
    "decode_hbar_address",
    "encode_hbar_address",
    "decode_hive_address",
    "encode_hive_address",
    "decode_hns_address",
    "encode_hns_address",
    "decode_hnt_address",
    "encode_hnt_address",
    "decode_icx_address",
    "encode_icx_address",
    "decode_iost_address",
    "encode_iost_address",
    "decode_iota_address",
    "encode_iota_address",
    "decode_iotx_address",
    "encode_iotx_address",
    "decode_iris_address",
    "encode_iris_address",
    "decode_kava_address",
    "encode_kava_address",
    "decode_kmd_address",
    "encode_kmd_address",
    "decode_ksm_address",
    "encode_ksm_address",
    "decode_lcc_address",
    "encode_lcc_address",
    "decode_lrg_address",
    "encode_lrg_address",
    "decode_lsk_address",
    "encode_lsk_address",
    "decode_ltc_address",
    "encode_ltc_address",
    "decode_luna_address",
    "encode_luna_address",
    "decode_mona_address",
    "encode_mona_address",
    "decode_mrx_address",
    "encode_mrx_address",
    "decode_nano_address",
    "encode_nano_address",
    "decode_nas_address",
    "encode_nas_address",
    "decode_near_address",
    "encode_near_address",
    "decode_neo_address",
    "encode_neo_address",
    "decode_nim_address",
    "encode_nim_address",
    "decode_nmc_address",
    "encode_nmc_address",
    "decode_nostr_address",
    "encode_nostr_address",
    "decode_nrgLegacy_address",
    "encode_nrgLegacy_address",
    "decode_nuls_address",
    "encode_nuls_address",
    "decode_one_address",
    "encode_one_address",
    "decode_ont_address",
    "encode_ont_address",
    "decode_poaLegacy_address",
    "encode_poaLegacy_address",
    "decode_ppc_address",
    "encode_ppc_address",
    "decode_qtum_address",
    "encode_qtum_address",
    "decode_rbtc_address",
    "encode_rbtc_address",
    "decode_rdd_address",
    "encode_rdd_address",
    "decode_rune_address",
    "encode_rune_address",
    "decode_rvn_address",
    "encode_rvn_address",
    "decode_sc_address",
    "encode_sc_address",
    "decode_sero_address",
    "encode_sero_address",
    "decode_sol_address",
    "encode_sol_address",
    "decode_srm_address",
    "encode_srm_address",
    "decode_steem_address",
    "encode_steem_address",
    "decode_strat_address",
    "encode_strat_address",
    "decode_strk_address",
    "encode_strk_address",
    "decode_stx_address",
    "encode_stx_address",
    "decode_sui_address",
    "encode_sui_address",
    "decode_sys_address",
    "encode_sys_address",
    "decode_tfuel_address",
    "encode_tfuel_address",
    "decode_thetaLegacy_address",
    "encode_thetaLegacy_address",
    "decode_tomoLegacy_address",
    "encode_tomoLegacy_address",
    "decode_trx_address",
    "encode_trx_address",
    "decode_ttLegacy_address",
    "encode_ttLegacy_address",
    "decode_vet_address",
    "encode_vet_address",
    "decode_via_address",
    "encode_via_address",
    "decode_vlx_address",
    "encode_vlx_address",
    "decode_vlxLegacy_address",
    "encode_vlxLegacy_address",
    "decode_vsys_address",
    "encode_vsys_address",
    "decode_wan_address",
    "encode_wan_address",
    "decode_waves_address",
    "encode_waves_address",
    "decode_wicc_address",
    "encode_wicc_address",
    "decode_xch_address",
    "encode_xch_address",
    "decode_xem_address",
    "encode_xem_address",
    "decode_xhv_address",
    "encode_xhv_address",
    "decode_xlm_address",
    "encode_xlm_address",
    "decode_xmr_address",
    "encode_xmr_address",
    "decode_xrp_address",
    "encode_xrp_address",
    "decode_xtz_address",
    "encode_xtz_address",
    "decode_xvg_address",
    "encode_xvg_address",
    "decode_zec_address",
    "encode_zec_address",
    "decode_zen_address",
    "encode_zen_address",
    "decode_zil_address",
    "encode_zil_address",
]
