
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2026-03-24, 20:31:42
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Committers:
-----------
| **These gerrit changes have been**

    - Verified
    - Not expired
    - Comments resolved
    - Approved by Maintainers

| **Please perform a final review & submit.**

  | `45181 <https:////gerrit.fd.io/r/c/vpp/+/45181>`_ [VECR 1]: hs-test: add messages to asserts

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer

bfd: **Klement Sekera** <klement.sekera@gmail.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

bufmon: **Benoît Ganne** <bganne@cisco.com>
  | `45110 <https:////gerrit.fd.io/r/c/vpp/+/45110>`_ [VECr 7]: bufmon: unregister old callbacks before re-registering on enable

build: **Damjan Marion** <damarion@cisco.com>
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VECr 18]: build: add Fedora 43 build compatibility
  | `45112 <https:////gerrit.fd.io/r/c/vpp/+/45112>`_ [VECr 18]: build: add AlmaLinux support to install-dep target
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer

classify: **Dave Barach** <vpp@barachs.net>
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 15]: tm: add 'mark_flow' action for traffic management

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VECr 27]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VECr 28]: cnat: fix show cnat client showing invalid for client id

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

crypto-infra: **Damjan Marion** <damarion@cisco.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoe: add PPPoE client and pppox
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoe: add PPPoE client and pppox
  | `44972 <https:////gerrit.fd.io/r/c/vpp/+/44972>`_ [VECr 0]: dpdk: call flow configure on device setup
  | `45114 <https:////gerrit.fd.io/r/c/vpp/+/45114>`_ [VECr 18]: dpdk: fix maybe-uninitialized warning with GCC 15

dpdk-cryptodev: **Kai Ji** <kai.ji@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 1]: ethernet: implement outer_vlan_id_any sub-interface matching

fib: **Neale Ranns** <neale@graphiant.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoe: add PPPoE client and pppox
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 5]: fib: honor unnumbered RX interface in MFIB RPF check

flow: **Damjan Marion** <damarion@cisco.com>
  | `45063 <https:////gerrit.fd.io/r/c/vpp/+/45063>`_ [VECr 5]: flow: fix flow_ops_function check

flowprobe: **Ole Troan** <otroan@employees.org>
  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VECr 13]: flowprobe: count based sampling support

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `45065 <https:////gerrit.fd.io/r/c/vpp/+/45065>`_ [VECr 0]: hsa: http masque support in builtin echo
  | `45299 <https:////gerrit.fd.io/r/c/vpp/+/45299>`_ [VECr 0]: quic: add support for tls profiles

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `45065 <https:////gerrit.fd.io/r/c/vpp/+/45065>`_ [VECr 0]: hsa: http masque support in builtin echo

interface: **Dave Barach** <vpp@barachs.net>
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 1]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 5]: interface: add global default rx-mode setting

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 3]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 11]: ip: add interface address change notifications

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 6]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 11]: ip: add interface address change notifications
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 15]: tm: add 'mark_flow' action for traffic management

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 5]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 5]: ip6-nd: enforce on-link source validation for ND learning
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 6]: ip6-nd: add punt reason for neigh advs
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 6]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 11]: ip6-nd: fix unicast NA handling in ND proxy
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 11]: ip6-nd: add nd-proxy all dst
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 19]: ip-neighbor: fix missing solicited-node multicast MAC

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45113 <https:////gerrit.fd.io/r/c/vpp/+/45113>`_ [VECr 18]: ipsec: fix implicit enum cast warnings with GCC 15
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

kube-test: **Florin Coras** <fcoras@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `45180 <https:////gerrit.fd.io/r/c/vpp/+/45180>`_ [VECr 4]: kube-test: add VppInstance struct and functions

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 1]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `44899 <https:////gerrit.fd.io/r/c/vpp/+/44899>`_ [VECr 6]: sr: implement sub-int L2 encap and DX2
  | `44970 <https:////gerrit.fd.io/r/c/vpp/+/44970>`_ [VECr 8]: l2: Add API for input/output features

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoe: add PPPoE client and pppox
  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VECr 4]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

lisp: **Florin Coras** <fcoras@cisco.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoe: add PPPoE client and pppox
  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VECr 6]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VECr 6]: stats: don't leak regcomp() allocated memory
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 11]: ip: add interface address change notifications
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VECr 18]: build: add Fedora 43 build compatibility
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `44985 <https:////gerrit.fd.io/r/c/vpp/+/44985>`_ [VECr 20]: nat: link test_pnat with pthread

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45161 <https:////gerrit.fd.io/r/c/vpp/+/45161>`_ [VECr 0]: octeon: fix device BAR4 mapping
  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VECr 15]: octeon: implement hardware traffic management
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

pg: **Dave Barach** <vpp@barachs.net>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 7]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 7]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 7]: policer: reject deletion of policer used by punt policing
  | `45203 <https:////gerrit.fd.io/r/c/vpp/+/45203>`_ [VECr 12]: policer: avoid redundant l2_overhead array access on TX path

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45299 <https:////gerrit.fd.io/r/c/vpp/+/45299>`_ [VECr 0]: quic: add support for tls profiles
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

sasc: **Ole Troan** <otroan@employees.org>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45115 <https:////gerrit.fd.io/r/c/vpp/+/45115>`_ [VECr 18]: sasc: fix maybe-uninitialized warning with GCC 15

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 0]: sfdp: guard packet bit shifts in lookup
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 5]: sfdp: offload lookup via vnet flow mark

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 5]: sfdp: offload lookup via vnet flow mark
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VECr 12]: sfdp: add blacklist/whitelist to snort service

snort: **Damjan Marion** <damarion@cisco.com>
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VECr 6]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VECr 6]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VECr 12]: sfdp: add blacklist/whitelist to snort service
  | `45116 <https:////gerrit.fd.io/r/c/vpp/+/45116>`_ [VECr 18]: snort: fix maybe-uninitialized warning with GCC 15

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `44899 <https:////gerrit.fd.io/r/c/vpp/+/44899>`_ [VECr 6]: sr: implement sub-int L2 encap and DX2

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 5]: interface: add global default rx-mode setting

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 1]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 3]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 5]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 5]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 5]: ip6-nd: enforce on-link source validation for ND learning
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 6]: ip6-nd: add punt reason for neigh advs
  | `44899 <https:////gerrit.fd.io/r/c/vpp/+/44899>`_ [VECr 6]: sr: implement sub-int L2 encap and DX2
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 6]: ip6-nd: add per-interface control for inbound RA acceptance
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 7]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 7]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 7]: policer: reject deletion of policer used by punt policing
  | `44970 <https:////gerrit.fd.io/r/c/vpp/+/44970>`_ [VECr 8]: l2: Add API for input/output features
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 11]: ip6-nd: fix unicast NA handling in ND proxy
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 11]: ip6-nd: add nd-proxy all dst
  | `44465 <https:////gerrit.fd.io/r/c/vpp/+/44465>`_ [VECr 13]: tests: support setting larger API queue size
  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VECr 13]: flowprobe: count based sampling support
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 19]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

vapi: **Ole Troan** <ot@cisco.com>
  | `44531 <https:////gerrit.fd.io/r/c/vpp/+/44531>`_ [VECr 13]: vapi: replace invalid chars in c macro name

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 1]: gso: implement IPv6 extension header traversal
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 5]: interface: add global default rx-mode setting

vpp: **Dave Barach** <vpp@barachs.net>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44546 <https:////gerrit.fd.io/r/c/vpp/+/44546>`_ [VECr 5]: vppapigen: error on use of array with unspecified length
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 5]: vppapigen: fix inconsistency in paths JSON

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VECr 29]: vxlan: reset next_dpo on delete

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `44745 <https:////gerrit.fd.io/r/c/vpp/+/44745>`_ [VECr 6]: wireguard: support for psk via v2 API messages
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VECr 27]: crypto: unify per-thread key_data allocation

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [Vec 124]: vhost: fix rxvq interrupts triggered because of race

**Andrew Mason** <mason12@gmail.com>:

  | `44082 <https:////gerrit.fd.io/r/c/vpp/+/44082>`_ [vec 137]: linux-cp: Punt for ISIS traffic over linux-cp plugin
  | `44085 <https:////gerrit.fd.io/r/c/vpp/+/44085>`_ [veC 138]: linux-cp: Punt for ISIS traffic over linux-cp plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 62]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 89]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features
  | `43916 <https:////gerrit.fd.io/r/c/vpp/+/43916>`_ [Vec 151]: vlib: print non-parked threads on vlib_worker_thread_barrier_sync_int
  | `43915 <https:////gerrit.fd.io/r/c/vpp/+/43915>`_ [Vec 154]: vnet: Initialize the classify arrays to ~0

**Aritra Basu** <aritrbas@cisco.com>:

  | `44981 <https:////gerrit.fd.io/r/c/vpp/+/44981>`_ [VeC 32]: ip-neighbor: preserve interface LL receive DPO for self link-local

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 89]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `45019 <https:////gerrit.fd.io/r/c/vpp/+/45019>`_ [vEC 2]: dpdk: improve error diagnostics
  | `39443 <https:////gerrit.fd.io/r/c/vpp/+/39443>`_ [vEC 25]: vnet: reorder vnet_buffer2 metadata
  | `44962 <https:////gerrit.fd.io/r/c/vpp/+/44962>`_ [VeC 34]: pppoe: initialize sw_if_index before early goto
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 41]: stats: show raw value in show stat segment

**C.J. Collier**:

  | `1948 <https:////gerrit.fd.io/r/c/vpp/+/1948>`_ [veC 151]: DO NOT MERGE - testing new build image

**Damjan Marion** <dmarion@0xa5.net>:

  | `44964 <https:////gerrit.fd.io/r/c/vpp/+/44964>`_ [VeC 32]: ethernet: add RSS callbacks
  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [veC 132]: ipsec: precompute payload and payload length adjustments
  | `44081 <https:////gerrit.fd.io/r/c/vpp/+/44081>`_ [veC 137]: ipsec: fill op templates with lengths and tag sizes

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [vEC 8]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [vEC 8]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Florin Coras** <florin.coras@gmail.com>:

  | `45298 <https:////gerrit.fd.io/r/c/vpp/+/45298>`_ [vEC 0]: tls: add ecdsa with X25519 test

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `44494 <https:////gerrit.fd.io/r/c/vpp/+/44494>`_ [vEC 0]: stats: vpp_get_stats: new options

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VEc 29]: sfdp: modify tenant_index type from u16 to u32
  | `44333 <https:////gerrit.fd.io/r/c/vpp/+/44333>`_ [VeC 76]: sasc: CLI command to enable/disable feature on intf
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 76]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VEc 0]: cnat: support encapsulation and session cleanup on backend deletion

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [veC 50]: tests: reduce sleep interval in ip-neighbor age test
  | `43891 <https:////gerrit.fd.io/r/c/vpp/+/43891>`_ [veC 160]: tests: add crypto+hmac perf test

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 46]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 46]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 46]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 46]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45290 <https:////gerrit.fd.io/r/c/vpp/+/45290>`_ [vEc 0]: tcp: pace jumbo connections with at least one MSS
  | `45102 <https:////gerrit.fd.io/r/c/vpp/+/45102>`_ [vEC 0]: sfdp: add configurable timer interval
  | `45285 <https:////gerrit.fd.io/r/c/vpp/+/45285>`_ [vEc 3]: tcp: avoid new data while sack holes remain
  | `45051 <https:////gerrit.fd.io/r/c/vpp/+/45051>`_ [VEc 11]: ip6: fix OOB read in HBH option processing
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VEc 13]: iavf: fix native AVF TSO queue setup
  | `45057 <https:////gerrit.fd.io/r/c/vpp/+/45057>`_ [VEc 18]: geneve: validate options_len field against buffer size
  | `44559 <https:////gerrit.fd.io/r/c/vpp/+/44559>`_ [VEc 21]: af_xdp: ensure null termination in format() string outputs
  | `44584 <https:////gerrit.fd.io/r/c/vpp/+/44584>`_ [veC 61]: tests: fix tag_fixme_debian12 to tag_fixme_debian11
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 73]: virtio: add native plugin L2 xconnect test with QEMU

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 47]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 163]: tests: add send_and_expect_multi

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [vEC 7]: policer: reject delete of policer still applied to interface
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [Vec 160]: ping: introduce traceroute tool

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VeC 104]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 104]: vcl: LDP default to regular option
  | `43874 <https:////gerrit.fd.io/r/c/vpp/+/43874>`_ [Vec 158]: unittest: add sfdp testing and unity framework

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44935 <https:////gerrit.fd.io/r/c/vpp/+/44935>`_ [VEc 6]: virtio: add support for mac filtering
  | `44930 <https:////gerrit.fd.io/r/c/vpp/+/44930>`_ [VEc 6]: virtio: add support for mac address changing
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 35]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 39]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 73]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 51]: iouring: Add io_uring plugin to allow polling usage of io_uring
  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [Vec 169]: af_xdp: allow usage of dynamic libbpf and libxdp
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [Vec 169]: af_xdp: introduce flag to allow SKB mode
  | `43611 <https:////gerrit.fd.io/r/c/vpp/+/43611>`_ [Vec 175]: build: use /usr/bin/env bash in checkstyle shebang instead of /bin/bash
  | `43760 <https:////gerrit.fd.io/r/c/vpp/+/43760>`_ [VeC 178]: rdma: allow dynamic libibverbs and libmlx5

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 34]: ip6-nd: support RA pfx info option with flag L&!A
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 35]: ip6: fix show ip6-ll cli if selector

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 53]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 54]: fix: correct fixstyle in session_sdl command function

**Ryosuke Nakayama** <ryosuke_666@icloud.com>:

  | `45117 <https:////gerrit.fd.io/r/c/vpp/+/45117>`_ [vEC 17]: atlantic: remove unused pkt_n_desc variable

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 88]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 96]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 111]: fib: dump by src not only contributing routes
  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [VeC 118]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VEc 4]: tm: add tm framework for hw traffic management

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 117]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 74]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 74]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 74]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 74]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 74]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 74]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 74]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 74]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 75]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 75]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 75]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 75]: vlib: mark cli quit command as mp_safe

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 89]: ip-neighbor: ARP/NA per-interface counter improvements

**echo** <614699596@qq.com>:

  | `45301 <https:////gerrit.fd.io/r/c/vpp/+/45301>`_ [vEC 0]: dpdk: preserve promiscuous mode when changing descriptors

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 42]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 46]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 99]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 21]: cnat: add scope_id to session key

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 41]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 86]: lb: fix incorrect byte order conversion for vip port display
  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [VeC 88]: lb: fix API byte order and IPv4 prefix length handling

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [veC 132]: ipsec: prevent use of deleted keys in async mode

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [vEC 19]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 74]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 57]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 57]: l2: fix null pointer access in l2-efp-filter

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          94
maintainers      57
committers       1
abandoned        0
================ ===

