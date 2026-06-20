from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.coins.abbc import abbc
from address_encoder.coins.ada import ada
from address_encoder.coins.ae import ae
from address_encoder.coins.aib import aib
from address_encoder.coins.aion import aion
from address_encoder.coins.algo import algo
from address_encoder.coins.ar import ar
from address_encoder.coins.ardr import ardr
from address_encoder.coins.ark import ark
from address_encoder.coins.atom import atom
from address_encoder.coins.avax import avax
from address_encoder.coins.bcd import bcd
from address_encoder.coins.bch import bch
from address_encoder.coins.bcn import bcn
from address_encoder.coins.bdx import bdx
from address_encoder.coins.bnb import bnb
from address_encoder.coins.bps import bps
from address_encoder.coins.bsv import bsv
from address_encoder.coins.btc import btc
from address_encoder.coins.btg import btg
from address_encoder.coins.btm import btm
from address_encoder.coins.bts import bts
from address_encoder.coins.cca import cca
from address_encoder.coins.ccxx import ccxx
from address_encoder.coins.celoLegacy import celoLegacy
from address_encoder.coins.ckb import ckb
from address_encoder.coins.cloLegacy import cloLegacy
from address_encoder.coins.dash import dash
from address_encoder.coins.dcr import dcr
from address_encoder.coins.dgb import dgb
from address_encoder.coins.divi import divi
from address_encoder.coins.doge import doge
from address_encoder.coins.dot import dot
from address_encoder.coins.egld import egld
from address_encoder.coins.ela import ela
from address_encoder.coins.eos import eos
from address_encoder.coins.etcLegacy import etcLegacy
from address_encoder.coins.eth import eth
from address_encoder.coins.etn import etn
from address_encoder.coins.ewtLegacy import ewtLegacy
from address_encoder.coins.fil import fil
from address_encoder.coins.fio import fio
from address_encoder.coins.firo import firo
from address_encoder.coins.flow import flow
from address_encoder.coins.flux import flux
from address_encoder.coins.ftmLegacy import ftmLegacy
from address_encoder.coins.gnoLegacy import gnoLegacy
from address_encoder.coins.goLegacy import goLegacy
from address_encoder.coins.grin import grin
from address_encoder.coins.gxc import gxc
from address_encoder.coins.hbar import hbar
from address_encoder.coins.hive import hive
from address_encoder.coins.hns import hns
from address_encoder.coins.hnt import hnt
from address_encoder.coins.icx import icx
from address_encoder.coins.iost import iost
from address_encoder.coins.iota import iota
from address_encoder.coins.iotx import iotx
from address_encoder.coins.iris import iris
from address_encoder.coins.kava import kava
from address_encoder.coins.kmd import kmd
from address_encoder.coins.ksm import ksm
from address_encoder.coins.lcc import lcc
from address_encoder.coins.lrg import lrg
from address_encoder.coins.lsk import lsk
from address_encoder.coins.ltc import ltc
from address_encoder.coins.luna import luna
from address_encoder.coins.mona import mona
from address_encoder.coins.mrx import mrx
from address_encoder.coins.nano import nano
from address_encoder.coins.nas import nas
from address_encoder.coins.near import near
from address_encoder.coins.neo import neo
from address_encoder.coins.nim import nim
from address_encoder.coins.nmc import nmc
from address_encoder.coins.nostr import nostr
from address_encoder.coins.nrgLegacy import nrgLegacy
from address_encoder.coins.nuls import nuls
from address_encoder.coins.one import one
from address_encoder.coins.ont import ont
from address_encoder.coins.poaLegacy import poaLegacy
from address_encoder.coins.ppc import ppc
from address_encoder.coins.qtum import qtum
from address_encoder.coins.rbtc import rbtc
from address_encoder.coins.rdd import rdd
from address_encoder.coins.rune import rune
from address_encoder.coins.rvn import rvn
from address_encoder.coins.sc import sc
from address_encoder.coins.sero import sero
from address_encoder.coins.sol import sol
from address_encoder.coins.srm import srm
from address_encoder.coins.steem import steem
from address_encoder.coins.strat import strat
from address_encoder.coins.strk import strk
from address_encoder.coins.stx import stx
from address_encoder.coins.sui import sui
from address_encoder.coins.sys import sys
from address_encoder.coins.tfuel import tfuel
from address_encoder.coins.thetaLegacy import thetaLegacy
from address_encoder.coins.tomoLegacy import tomoLegacy
from address_encoder.coins.trx import trx
from address_encoder.coins.ttLegacy import ttLegacy
from address_encoder.coins.vet import vet
from address_encoder.coins.via import via
from address_encoder.coins.vlx import vlx
from address_encoder.coins.vlxLegacy import vlxLegacy
from address_encoder.coins.vsys import vsys
from address_encoder.coins.wan import wan
from address_encoder.coins.waves import waves
from address_encoder.coins.wicc import wicc
from address_encoder.coins.xch import xch
from address_encoder.coins.xem import xem
from address_encoder.coins.xhv import xhv
from address_encoder.coins.xlm import xlm
from address_encoder.coins.xmr import xmr
from address_encoder.coins.xrp import xrp
from address_encoder.coins.xtz import xtz
from address_encoder.coins.xvg import xvg
from address_encoder.coins.zec import zec
from address_encoder.coins.zen import zen
from address_encoder.coins.zil import zil

COINS: dict[str, CoinCoder] = {
    "abbc": abbc,
    "ada": ada,
    "ae": ae,
    "aib": aib,
    "aion": aion,
    "algo": algo,
    "ar": ar,
    "ardr": ardr,
    "ark": ark,
    "atom": atom,
    "avax": avax,
    "bcd": bcd,
    "bch": bch,
    "bcn": bcn,
    "bdx": bdx,
    "bnb": bnb,
    "bps": bps,
    "bsv": bsv,
    "btc": btc,
    "btg": btg,
    "btm": btm,
    "bts": bts,
    "cca": cca,
    "ccxx": ccxx,
    "celoLegacy": celoLegacy,
    "ckb": ckb,
    "cloLegacy": cloLegacy,
    "dash": dash,
    "dcr": dcr,
    "dgb": dgb,
    "divi": divi,
    "doge": doge,
    "dot": dot,
    "egld": egld,
    "ela": ela,
    "eos": eos,
    "etcLegacy": etcLegacy,
    "eth": eth,
    "etn": etn,
    "ewtLegacy": ewtLegacy,
    "fil": fil,
    "fio": fio,
    "firo": firo,
    "flow": flow,
    "flux": flux,
    "ftmLegacy": ftmLegacy,
    "gnoLegacy": gnoLegacy,
    "goLegacy": goLegacy,
    "grin": grin,
    "gxc": gxc,
    "hbar": hbar,
    "hive": hive,
    "hns": hns,
    "hnt": hnt,
    "icx": icx,
    "iost": iost,
    "iota": iota,
    "iotx": iotx,
    "iris": iris,
    "kava": kava,
    "kmd": kmd,
    "ksm": ksm,
    "lcc": lcc,
    "lrg": lrg,
    "lsk": lsk,
    "ltc": ltc,
    "luna": luna,
    "mona": mona,
    "mrx": mrx,
    "nano": nano,
    "nas": nas,
    "near": near,
    "neo": neo,
    "nim": nim,
    "nmc": nmc,
    "nostr": nostr,
    "nrgLegacy": nrgLegacy,
    "nuls": nuls,
    "one": one,
    "ont": ont,
    "poaLegacy": poaLegacy,
    "ppc": ppc,
    "qtum": qtum,
    "rbtc": rbtc,
    "rdd": rdd,
    "rune": rune,
    "rvn": rvn,
    "sc": sc,
    "sero": sero,
    "sol": sol,
    "srm": srm,
    "steem": steem,
    "strat": strat,
    "strk": strk,
    "stx": stx,
    "sui": sui,
    "sys": sys,
    "tfuel": tfuel,
    "thetaLegacy": thetaLegacy,
    "tomoLegacy": tomoLegacy,
    "trx": trx,
    "ttLegacy": ttLegacy,
    "vet": vet,
    "via": via,
    "vlx": vlx,
    "vlxLegacy": vlxLegacy,
    "vsys": vsys,
    "wan": wan,
    "waves": waves,
    "wicc": wicc,
    "xch": xch,
    "xem": xem,
    "xhv": xhv,
    "xlm": xlm,
    "xmr": xmr,
    "xrp": xrp,
    "xtz": xtz,
    "xvg": xvg,
    "zec": zec,
    "zen": zen,
    "zil": zil
}
