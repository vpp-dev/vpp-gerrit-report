#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

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
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2026-06-13, 05:44:58
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

  | `45965 <https:////gerrit.fd.io/r/c/vpp/+/45965>`_ [VECR 2]: tests: pg: add maxframe parameter
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VECR 4]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VECR 4]: cnat: fix show cnat translation for specific translation id

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 1]: vlib: ASAN-poison unallocated buffers

build: **Damjan Marion** <damarion@cisco.com>
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VECr 0]: build: include GNUInstallDirs in VPPConfig
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 8]: dpdk: install default jump-to-group-1 rule for mlx5

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 23]: cnat: add scope_id to session key

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 1]: crypto: add op tracing capability

dev: **Damjan Marion** <damarion@cisco.com>
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 1]: flow: implement VNET_FLOW_ACTION_COUNT operation

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 22]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 23]: cnat: add scope_id to session key
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 30]: rdma: add mlx5 TSO support for raw packet tx

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 1]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 1]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 1]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 1]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 8]: dpdk: install default jump-to-group-1 rule for mlx5

flow: **Damjan Marion** <damarion@cisco.com>
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VECr 1]: flow: add APIs to support new flow actions
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 1]: flow: add parameter to pre-allocate global pool
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 1]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 1]: flow: add flow aging support
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 2]: flow: add flow template and async range infrastructure
  | `45908 <https:////gerrit.fd.io/r/c/vpp/+/45908>`_ [VECr 10]: flow: add max parameter in 'show flow entry' CLI

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 1]: tls: propagate verify config for dtls
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 17]: vlib: fix process state format output wrapped by extra quotes
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 29]: tls: add ALPN negotiation support

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 21]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 0]: interface: enable IPv6 link state on unnumbered interfaces
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 1]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 2]: flow: add flow template and async range infrastructure

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `46000 <https:////gerrit.fd.io/r/c/vpp/+/46000>`_ [VECr 7]: ip6: fix potential small OOB read in extension header walk
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 9]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 9]: ip: fix adjacent packet overwrite with ip6 frags
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 28]: ip: svr add bit indicating fragmentation to vnet_buffer

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [VECr 1]: ip6-nd: fix crash in link-local target NS

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 1]: crypto: add op tracing capability

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45961 <https:////gerrit.fd.io/r/c/vpp/+/45961>`_ [VECr 0]: hsa: handle vperf client session closes/resets
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VECr 0]: hsa: fix builtin cut-through
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 1]: crypto: add op tracing capability
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 28]: ip: svr add bit indicating fragmentation to vnet_buffer

npol: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Hedi Bouattour** <hedibouattour2010@gmail.com>
  | `46046 <https:////gerrit.fd.io/r/c/vpp/+/46046>`_ [VECr 0]: npol: fix interface name parsing

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VECr 28]: octeon: add PFC support

pvti: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45956 <https:////gerrit.fd.io/r/c/vpp/+/45956>`_ [VECr 4]: pvti: fix adjacent packet overwrite with very big packets

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 30]: rdma: add mlx5 TSO support for raw packet tx

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 25]: sfdp: fix specification of scope_index

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 22]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45915 <https:////gerrit.fd.io/r/c/vpp/+/45915>`_ [VECr 1]: snort: fix wrong variable reference
  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VECr 21]: snort: don't store snort metadata in buffer

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46014 <https:////gerrit.fd.io/r/c/vpp/+/46014>`_ [VECr 0]: tests: add extra_vpp_heap_config knob for main-heap-size
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 1]: vlib: ASAN-poison unallocated buffers
  | `46000 <https:////gerrit.fd.io/r/c/vpp/+/46000>`_ [VECr 7]: ip6: fix potential small OOB read in extension header walk
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 22]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 23]: cnat: add scope_id to session key
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 25]: sfdp: fix specification of scope_index
  | `45837 <https:////gerrit.fd.io/r/c/vpp/+/45837>`_ [VECr 29]: tests: add suffix to failed_test file
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 29]: tls: add ALPN negotiation support

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VECr 1]: tls: propagate verify config for dtls
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 29]: tls: add ALPN negotiation support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VECr 0]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 17]: vlib: fix process state format output wrapped by extra quotes

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 22]: sfdp: add sfdp-session-stats service

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VECr 16]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VeC 42]: ip_validate: new plugin to drop packets with invalid addresses

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 73]: vhost: fix rxvq interrupts triggered because of race

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 142]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 44]: map: enhance map plugin to support per-vrf rules

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 170]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VEc 0]: tcp: add TCP fast open support (RFC 7413)
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [vEc 7]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 84]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 86]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 86]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 86]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 86]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 92]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 170]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 7]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46035 <https:////gerrit.fd.io/r/c/vpp/+/46035>`_ [vEC 0]: tests: remove tag_fixme_debian12

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 88]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 88]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VEc 1]: buffers: return values; improve debug
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 37]: dpdk: tracing improvements

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45937 <https:////gerrit.fd.io/r/c/vpp/+/45937>`_ [vEC 0]: tracepath: add api to dump trace paths
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [vEC 1]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 1]: sfdp: add verdict-testbench service
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [vEC 1]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [VEc 4]: tracepath: minor refactoring to code
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [Vec 45]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 109]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 156]: sasc: fix tenant_index overlap in sasc_buffer

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [vEC 1]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `45696 <https:////gerrit.fd.io/r/c/vpp/+/45696>`_ [VEc 2]: cnat: make cnat pluggable
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VEc 4]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get
  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VeC 38]: npol: wire npol into the cnat slow-path hook mechanism

**Ivan Ivanets** <iivanets@cisco.com>:

  | `46044 <https:////gerrit.fd.io/r/c/vpp/+/46044>`_ [vEC 1]: vcl: guard QUIC connection close error-code
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 78]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 107]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 126]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 126]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 126]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 126]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 31]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 31]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 31]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 45]: virtio: add native plugin L2 xconnect test with QEMU
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VeC 46]: af_xdp: add support for multi-buffer

**Jiajun Liang** <3138947285@qq.com>:

  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [vEC 1]: linux-cp: guard PPPOX interface type and tolerate missing neighbor
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [vEC 1]: rdma: steer PPPoE discovery and session flows
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [vEC 1]: dhcp: export DHCPv6 runtime state for PPPoE observability

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VEc 2]: ip bonding hash: inner-aware flow hash (opt-in)

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 128]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 70]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 70]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [vEC 5]: api: add build-time python stub generation via vppapigen
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 51]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 1]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 1]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Maxime Peim** <maxime.peim@gmail.com>:

  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VEc 2]: vlib: add per-thread pool cache primitive
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [vEC 2]: docs: document build-time VPP parameters
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vEc 8]: flow: add per-thread flow pool cache for multi-worker safety
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEC 8]: dpdk: support async flow offload
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [vEC 8]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 81]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 81]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 87]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 87]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 87]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 87]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 21]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 66]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 86]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 92]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 115]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 119]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 154]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 132]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 65]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 65]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 73]: ip6: fix show ip6-ll cli if selector
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 109]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 114]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 8]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 58]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 133]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 135]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 65]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [VEc 16]: pfc: add framework for priority flow control

**Robert Shearman** <robertshearman@gmail.com>:

  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [VEc 3]: misc: fix potential OOB read during flow hash calculations
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 42]: vppapigen: fix inconsistency in paths JSON

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `45917 <https:////gerrit.fd.io/r/c/vpp/+/45917>`_ [VEc 9]: linux-cp: mcast ospf test
  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 73]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 168]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 176]: linux-cp: on remove do cleanup for all fibs

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 25]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 73]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 154]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 154]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 154]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 154]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 154]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 155]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 155]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 155]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 155]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 155]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 155]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 155]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vEc 14]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 58]: empty change for GHA(CSIT) testing

**Wayne Morrison** <wmorrison@netgate.com>:

  | `45949 <https:////gerrit.fd.io/r/c/vpp/+/45949>`_ [VEc 0]: lldp: extend data returned by lldp-dump API

**Wei Wang** <weiwaus@gmail.com>:

  | `46025 <https:////gerrit.fd.io/r/c/vpp/+/46025>`_ [VEc 1]: tls: tls session resumption code and host stack tests

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 170]: ip-neighbor: ARP/NA per-interface counter improvements

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [VEc 16]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [vEC 17]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vEc 23]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VEc 2]: vppinfra: add loongarch64 architecture support

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 77]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 122]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 32]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 73]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 73]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 74]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 127]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 46]: fib: compute fib entry flags from full path list

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 85]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 73]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 73]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 167]: lb: fix incorrect byte order conversion for vip port display

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 42]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 31]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 32]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 38]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 155]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 137]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 137]: l2: fix null pointer access in l2-efp-filter

**yewtow** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VeC 60]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VeC 61]: ip6-nd: support RDNSS option in IPv6 RA

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
authors          135
maintainers      40
committers       3
abandoned        0
================ ===

