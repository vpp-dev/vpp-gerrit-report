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
generated on Sunday 2023-02-19, 02:33:12
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


Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 9]: af_xdp: optimizing send performance
  | `38059 <https:////gerrit.fd.io/r/c/vpp/+/38059>`_ [VECr 16]: af_xdp: fix netns configuration

avf: **Damjan Marion** <damarion@cisco.com>
  | `38200 <https:////gerrit.fd.io/r/c/vpp/+/38200>`_ [VECr 8]: avf: fix cli memory leak with incorrect options

build: **Damjan Marion** <damarion@cisco.com>
  | `38147 <https:////gerrit.fd.io/r/c/vpp/+/38147>`_ [VECr 5]: build: add Rocky Linux 9 support
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 16]: dpdk: bump to dpdk 22.11
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 25]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VECr 29]: classify: bypass drop filter on specific error

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag
  | `37871 <https:////gerrit.fd.io/r/c/vpp/+/37871>`_ [VECr 16]: crypto: make it easier to diagnose keys use-after-free

crypto-ipsecmb: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag

crypto-native: **Damjan Marion** <damarion@cisco.com>
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 25]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 16]: dpdk: bump to dpdk 22.11
  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VECr 22]: dpdk: fix compatibility with DPDK < 21.11

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 16]: dpdk: bump to dpdk 22.11

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 8]: misc: fix feature dispatch possible crashed when feature config changed by user

fib: **Neale Ranns** <neale@graphiant.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `38293 <https:////gerrit.fd.io/r/c/vpp/+/38293>`_ [VECr 1]: hs-test: rearrange veth interfaces used in bridge

interface: **Dave Barach** <vpp@barachs.net>
  | `38045 <https:////gerrit.fd.io/r/c/vpp/+/38045>`_ [VECr 23]: interface: add the missing tag keyword in the cli helper
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VECr 29]: classify: bypass drop filter on specific error

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `38139 <https:////gerrit.fd.io/r/c/vpp/+/38139>`_ [VECr 9]: vnet: throttling configuration improvement

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 2]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 2]: ip: Set the buffer error in ip6-input
  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VECr 2]: ip: fix update checksum in ip4_ttl_inc
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 8]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `38139 <https:////gerrit.fd.io/r/c/vpp/+/38139>`_ [VECr 9]: vnet: throttling configuration improvement

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VECr 3]: ipsec: esp_encrypt prefetch and unroll
  | `38252 <https:////gerrit.fd.io/r/c/vpp/+/38252>`_ [VECr 4]: ipsec: set fast path 5tuple ip addresses based on sa traffic selector values

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VECr 18]: lb: fix flow table update vector handing with ASAN
  | `38048 <https:////gerrit.fd.io/r/c/vpp/+/38048>`_ [VECr 22]: lb: keep AddressSanitizer happy

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 24]: libmemif: added tests

memif: **Damjan Marion** <damarion@cisco.com>
  | `37912 <https:////gerrit.fd.io/r/c/vpp/+/37912>`_ [VECr 2]: memif: fix input vector rate of memif-input node
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VECr 2]: memif: autogenerate socket_ids

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38298 <https:////gerrit.fd.io/r/c/vpp/+/38298>`_ [VECr 1]: stats: expose symlink to stats client
  | `38147 <https:////gerrit.fd.io/r/c/vpp/+/38147>`_ [VECr 5]: build: add Rocky Linux 9 support
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 8]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `38139 <https:////gerrit.fd.io/r/c/vpp/+/38139>`_ [VECr 9]: vnet: throttling configuration improvement
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag
  | `38148 <https:////gerrit.fd.io/r/c/vpp/+/38148>`_ [VECr 10]: misc: define SElinux mapped file permissions
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 25]: fateshare: a plugin for managing child processes

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 4]: mpls: fix possible crashes on tunnel create/delete

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VECr 8]: misc: fix feature dispatch possible crashed when feature config changed by user

session: **Florin Coras** <fcoras@cisco.com>
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 18]: session: consolidate port alloc logic

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 6]: srv6-mobile: Implement SRv6 mobile API funcs

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38292 <https:////gerrit.fd.io/r/c/vpp/+/38292>`_ [VECr 1]: tcp: allow syns in closed state
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 18]: session: consolidate port alloc logic

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 2]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VECr 2]: ip: Set the buffer error in ip6-input
  | `38250 <https:////gerrit.fd.io/r/c/vpp/+/38250>`_ [VECr 4]: vppinfra: fix clib_bitmap_will_expand() result inversion
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 4]: mpls: fix possible crashes on tunnel create/delete
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 6]: srv6-mobile: Implement SRv6 mobile API funcs
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VECr 23]: tests: refactor extra_vpp_punt_config

udp: **Florin Coras** <fcoras@cisco.com>
  | `38080 <https:////gerrit.fd.io/r/c/vpp/+/38080>`_ [VECr 18]: session: consolidate port alloc logic

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `34966 <https:////gerrit.fd.io/r/c/vpp/+/34966>`_ [VECr 10]: crypto: remove VNET_CRYPTO_OP_FLAG_INIT_IV flag

vcl: **Florin Coras** <fcoras@cisco.com>
  | `38167 <https:////gerrit.fd.io/r/c/vpp/+/38167>`_ [VECr 1]: vcl: ldp support for ip_pktinfo
  | `38287 <https:////gerrit.fd.io/r/c/vpp/+/38287>`_ [VECr 2]: vcl: fix incorrect ldp worker in ldp_epoll_pwait()
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 3]: misc: patch to test CI infra changes
  | `38155 <https:////gerrit.fd.io/r/c/vpp/+/38155>`_ [VECr 11]: vcl: improve vls handling of shared listeners
  | `38162 <https:////gerrit.fd.io/r/c/vpp/+/38162>`_ [VECr 11]: vcl: handle lt events in epoll ctl

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38196 <https:////gerrit.fd.io/r/c/vpp/+/38196>`_ [VECr 9]: vppinfra: display only the 1st 50 memory traces by default
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VECr 22]: stats: fix node name compatison

vpp-swan: **Fan Zhang** <roy.fan.zhang@intel.com>, **Gabriel Oginski** <gabrielx.oginski@intel.com>
  | `38253 <https:////gerrit.fd.io/r/c/vpp/+/38253>`_ [VECr 4]: vpp-swan: fix segmentation fault in arp function

vppapigen: **Ole Troan** <otroan@employees.org>
  | `38284 <https:////gerrit.fd.io/r/c/vpp/+/38284>`_ [VECr 3]: build: check for presence of python ply

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `38282 <https:////gerrit.fd.io/r/c/vpp/+/38282>`_ [VECr 2]: vppinfra: adding support for socket mounting paths
  | `38196 <https:////gerrit.fd.io/r/c/vpp/+/38196>`_ [VECr 9]: vppinfra: display only the 1st 50 memory traces by default
  | `38175 <https:////gerrit.fd.io/r/c/vpp/+/38175>`_ [VECr 10]: vppinfra: fix memory traces

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 166]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 169]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [vEC 22]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 68]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 88]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [vEC 1]: ipsec: add per-SA error counters
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 61]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 165]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `34965 <https:////gerrit.fd.io/r/c/vpp/+/34965>`_ [VEc 1]: ipsec: make pre-shared keys harder to misuse
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 130]: build: add sanitizer option to configure script

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 24]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 2]: dpdk-cryptodev: enq/deq scheme rework
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [VEc 3]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [Vec 93]: tests: remove intermittent failing tests on vpp_debug image

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 72]: stats: fix memory leak in stat_segment_dump_r()

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 127]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 115]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 115]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 115]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 115]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 115]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 115]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `38254 <https:////gerrit.fd.io/r/c/vpp/+/38254>`_ [VEc 1]: vpp-swan: fix memory leaks
  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 11]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 40]: interface: fix crash if vnet_hw_if_get_rx_queue return zero
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 40]: nat: nat44-ed get out2in workers failed for static mapping without port

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 144]: urpf: add show urpf cli

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 66]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 77]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 88]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 88]: classify: fix classify session cli.

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 115]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 115]: nat: fix nat44-ed API
  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 171]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 133]: memif: fix uninitialized variable warning

**Klement Sekera** <klement.sekera@gmail.com>:

  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VEc 5]: tests: enhance counter comparison error message

**Leyi Rong** <leyi.rong@intel.com>:

  | `37853 <https:////gerrit.fd.io/r/c/vpp/+/37853>`_ [VeC 58]: avf: performance optimization when CLIB_HAVE_VEC512 is enabled

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37691 <https:////gerrit.fd.io/r/c/vpp/+/37691>`_ [VeC 51]: vlib: fix vlib_log for elog

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [VEc 5]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VEc 24]: ipsec: huge anti-replay window support

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 74]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 115]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 129]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 135]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 141]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 141]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 141]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 141]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 141]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 141]: cnat: flag to disable rsession
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 141]: memif: add support for ns abstract sockets

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 2]: ip: IP address family common input node

**Ole Troan** <otroan@employees.org>:

  | `37766 <https:////gerrit.fd.io/r/c/vpp/+/37766>`_ [veC 66]: papi: vla list of fixed strings

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 115]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [VEc 25]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 179]: ip6-nd: add fixed flag

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37939 <https:////gerrit.fd.io/r/c/vpp/+/37939>`_ [VEc 16]: ip: support flow-hash gtpv1teid

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 115]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 142]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 154]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 113]: dpdk: fix interface name w/ the same PCI bus/slot/function

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 115]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [VeC 75]: vlib: avoid non-mp-safe cli process node updates
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 82]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 115]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VeC 115]: nat: fix nat44-ed outside address distribution
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 143]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 149]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 149]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 33]: api: fix vl_socket_write_ready
  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 157]: avf: tolerate socket events in avf_process_request

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 31]: api: fix api msg thread safe setting not work
  | `37793 <https:////gerrit.fd.io/r/c/vpp/+/37793>`_ [VeC 68]: dpdk: plugin init should be protect by thread barrier
  | `37789 <https:////gerrit.fd.io/r/c/vpp/+/37789>`_ [VeC 70]: vlib: fix ASAN fake stack size set error when switching to process
  | `37777 <https:////gerrit.fd.io/r/c/vpp/+/37777>`_ [VeC 72]: stats: fix node name compare error when updating stats segment
  | `37776 <https:////gerrit.fd.io/r/c/vpp/+/37776>`_ [VeC 72]: vlib: fix macro define command not work in startup config exec script
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VeC 81]: crypto: fix async frame memory crash if frame pool expanded when using
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 84]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 115]: nat: auto forward inbound packet for local server session app with snat
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 120]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 125]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 132]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 133]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 173]: arp: add support for Microsoft NLB unicast

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 170]: ip: fixup crash when reassemble a lots of fragments.

**Yong Liu** <yong.liu@intel.com>:

  | `37821 <https:////gerrit.fd.io/r/c/vpp/+/37821>`_ [Vec 67]: session: map new segment when dma enabled
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VeC 67]: vlib: pre-alloc dma batch structure
  | `37823 <https:////gerrit.fd.io/r/c/vpp/+/37823>`_ [veC 67]: memif: support dma option
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VeC 67]: vlib: support dma map extended memory
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VeC 67]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VeC 67]: dma_intel: add native dsa device driver

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [VEc 4]: af_xdp: change default queue size as kernel xsk default

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 156]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 95]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 98]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 83]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 103]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [Vec 115]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 129]: vppinfra: add time error counters to stats segment

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
authors          99
maintainers      44
committers       0
abandoned        0
================ ===

