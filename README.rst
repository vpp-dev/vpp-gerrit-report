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
generated on Friday 2022-12-16, 02:13:54
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

  | `37795 <https:////gerrit.fd.io/r/c/vpp/+/37795>`_ [VECR 0]: bfd: fix bfd udp error enum incompatibility
  | `37683 <https:////gerrit.fd.io/r/c/vpp/+/37683>`_ [VECR 1]: nat: fix memory leak and refactor nat44-ed db init/free.
  | `37745 <https:////gerrit.fd.io/r/c/vpp/+/37745>`_ [VECR 1]: nat: fix incorrect using about sw_if_index in nat44-ed static mapping v2 api.

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VECr 23]: acl: change the algorithm for cleaning the sessions from purgatory

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 3]: af_xdp: optimizing send performance

api: **Dave Barach** <vpp@barachs.net>
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [VECr 2]: api: fix api msg thread safe setting not work

build: **Damjan Marion** <damarion@cisco.com>
  | `37825 <https:////gerrit.fd.io/r/c/vpp/+/37825>`_ [VECr 2]: build: cmake NAMELINK_COMPONENT in vpp libraries
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 23]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VECr 23]: classify: fix classify session cli.

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 10]: ipsec: add per-SA error counters
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 16]: crypto: fix async frame memory crash if frame pool expanded when using

dma_intel: **Marvin Liu** <yong.liu@intel.com>
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 2]: vlib: pre-alloc dma batch structure
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VECr 2]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 2]: dma_intel: add native dsa device driver

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 10]: pci: add option to force uio binding
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 13]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `37793 <https:////gerrit.fd.io/r/c/vpp/+/37793>`_ [VECr 3]: dpdk: plugin init should be protect by thread barrier
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 6]: vxlan: convert vxlan to a plugin
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 10]: pci: add option to force uio binding

fib: **Neale Ranns** <neale@graphiant.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 13]: ip_session_redirect: add session redirect plugin

interface: **Dave Barach** <vpp@barachs.net>
  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VECr 10]: vppapigen: enable codegen for stream message types

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [VECr 2]: api: fix api msg thread safe setting not work
  | `37690 <https:////gerrit.fd.io/r/c/vpp/+/37690>`_ [VECr 10]: ip: fix ip ACL traces

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 10]: ipsec: add per-SA error counters
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 16]: crypto: fix async frame memory crash if frame pool expanded when using
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 27]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [VECr 2]: api: fix api msg thread safe setting not work

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 6]: vxlan: convert vxlan to a plugin
  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VECr 7]: stats: fix memory leak in stat_segment_dump_r()
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 13]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37788 <https:////gerrit.fd.io/r/c/vpp/+/37788>`_ [VECr 6]: nat: fix accidental o2i deletion/reuse
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 17]: nat: fix nat44_ed set_session_limit crash

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 6]: vxlan: convert vxlan to a plugin

pci: **Damjan Marion** <damarion@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 10]: pci: add option to force uio binding

policer: **Neale Ranns** <neale@graphiant.com>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 23]: policer: fix crash when delete interface policer classify.

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `37779 <https:////gerrit.fd.io/r/c/vpp/+/37779>`_ [VECr 0]: pppoe: fix memcpy out of bounds with gcc-11 on arm

session: **Florin Coras** <fcoras@cisco.com>
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 2]: vlib: pre-alloc dma batch structure

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37829 <https:////gerrit.fd.io/r/c/vpp/+/37829>`_ [VECr 1]: tests: support tmp-dir on different filesystem
  | `37788 <https:////gerrit.fd.io/r/c/vpp/+/37788>`_ [VECr 6]: nat: fix accidental o2i deletion/reuse
  | `37672 <https:////gerrit.fd.io/r/c/vpp/+/37672>`_ [VECr 10]: ipsec: fix SA names consistency in tests
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 10]: ipsec: add per-SA error counters
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 13]: ip_session_redirect: add session redirect plugin
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 17]: nat: fix nat44_ed set_session_limit crash
  | `37268 <https:////gerrit.fd.io/r/c/vpp/+/37268>`_ [VECr 21]: lb: add source ip based sticky load balancing
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 27]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation

vapi: **Ole Troan** <ot@cisco.com>
  | `37817 <https:////gerrit.fd.io/r/c/vpp/+/37817>`_ [VECr 0]: vapi: use the correct my_context_id when disconnecting API clients

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 23]: misc: patch to test CI infra changes

vhost: **Steven Luong** <sluong@cisco.com>
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [VECr 2]: api: fix api msg thread safe setting not work

virtio: **Mohsin Kazmi** <sykazmi@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37416 <https:////gerrit.fd.io/r/c/vpp/+/37416>`_ [VECr 10]: virtio: add option to bind interface to uio driver

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37819 <https:////gerrit.fd.io/r/c/vpp/+/37819>`_ [VECr 2]: vlib: pre-alloc dma batch structure
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VECr 2]: vlib: support dma map extended memory
  | `37691 <https:////gerrit.fd.io/r/c/vpp/+/37691>`_ [VECr 2]: vlib: fix vlib_log for elog
  | `37789 <https:////gerrit.fd.io/r/c/vpp/+/37789>`_ [VECr 5]: vlib: fix ASAN fake stack size set error when switching to process
  | `37777 <https:////gerrit.fd.io/r/c/vpp/+/37777>`_ [VECr 7]: stats: fix node name compare error when updating stats segment
  | `37776 <https:////gerrit.fd.io/r/c/vpp/+/37776>`_ [VECr 7]: vlib: fix macro define command not work in startup config exec script
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 10]: pci: add option to force uio binding
  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [VECr 10]: vlib: avoid non-mp-safe cli process node updates

vmxnet3: **Steven Luong** <sluong@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 10]: pci: add option to force uio binding

vpp: **Dave Barach** <vpp@barachs.net>
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VECr 2]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 2]: dma_intel: add native dsa device driver

vppapigen: **Ole Troan** <otroan@employees.org>
  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VECr 10]: vppapigen: enable codegen for stream message types

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37763 <https:////gerrit.fd.io/r/c/vpp/+/37763>`_ [VECr 6]: wireguard: add local variable
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 16]: crypto: fix async frame memory crash if frame pool expanded when using

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 101]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 104]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VEc 3]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `31368 <https:////gerrit.fd.io/r/c/vpp/+/31368>`_ [Vec 176]: vlib: Sleep less in unix input if there were active signals recently

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37059 <https:////gerrit.fd.io/r/c/vpp/+/37059>`_ [VEc 0]: ipsec: new api for sa ips and ports updates
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 29]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 100]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `37742 <https:////gerrit.fd.io/r/c/vpp/+/37742>`_ [VEc 1]: nat: do not use nat session object after deletion
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 65]: build: add sanitizer option to configure script

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `36705 <https:////gerrit.fd.io/r/c/vpp/+/36705>`_ [VeC 140]: ip-neighbor: Fixed delay(1~2s) in neighbor-probe interval

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [VEc 0]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 103]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [VEc 28]: tests: remove intermittent failing tests on vpp_debug image

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 62]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 50]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 50]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 50]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 50]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 50]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 50]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 3]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 36]: interface: fix crash if vnet_hw_if_get_rx_queue return zero
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 50]: nat: nat44-ed get out2in workers failed for static mapping without port

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 79]: urpf: add show urpf cli
  | `34726 <https:////gerrit.fd.io/r/c/vpp/+/34726>`_ [VeC 132]: interface: add buffer stats api

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [VEc 1]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [VEc 12]: nat: fix crash when set nat44 session limit with nonexisted vrf.

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `36592 <https:////gerrit.fd.io/r/c/vpp/+/36592>`_ [VeC 163]: stats: handle interface renames properly
  | `36590 <https:////gerrit.fd.io/r/c/vpp/+/36590>`_ [VeC 163]: nat: fix handling checksum offload in nat44-ed

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 50]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 50]: nat: fix nat44-ed API
  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 106]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 68]: memif: fix uninitialized variable warning

**Klement Sekera** <klement.sekera@gmail.com>:

  | `37654 <https:////gerrit.fd.io/r/c/vpp/+/37654>`_ [VeC 31]: tests: improve packet checksum functions

**Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>:

  | `37832 <https:////gerrit.fd.io/r/c/vpp/+/37832>`_ [VEc 0]: hs-test: abstract away topology from test cases

**Mercury Noah** <mercury124185@gmail.com>:

  | `36492 <https:////gerrit.fd.io/r/c/vpp/+/36492>`_ [VeC 174]: ip6-nd: fix ip6-nd proxy issue

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [VEc 9]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 50]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 64]: vlib: introduce an inter worker interrupts efds

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `37830 <https:////gerrit.fd.io/r/c/vpp/+/37830>`_ [VEc 0]: af_packet: move to plugin

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 70]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 76]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 76]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 76]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 76]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 76]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 76]: cnat: flag to disable rsession
  | `35805 <https:////gerrit.fd.io/r/c/vpp/+/35805>`_ [VeC 76]: dpdk: add intf tag to dev{} subinput
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 76]: memif: add support for ns abstract sockets
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VeC 150]: memif: autogenerate socket_ids

**Neale Ranns** <neale@graphiant.com>:

  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 126]: vlib: "sh errors" shows error severity counters

**Ole Troan** <otroan@employees.org>:

  | `37766 <https:////gerrit.fd.io/r/c/vpp/+/37766>`_ [vEC 1]: papi: vla list of fixed strings

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `37678 <https:////gerrit.fd.io/r/c/vpp/+/37678>`_ [VEc 27]: fib: partial fix to a deadlock during CSIT tests execution

**RADHA KRISHNA SARAGADAM** <krishna_srk2003@yahoo.com>:

  | `36711 <https:////gerrit.fd.io/r/c/vpp/+/36711>`_ [Vec 142]: ebuild: upgrade vagrant ubuntu version to 20.04

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 50]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 101]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 114]: ip6-nd: add fixed flag

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VEc 2]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 50]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 77]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 89]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 48]: dpdk: fix interface name w/ the same PCI bus/slot/function
  | `36488 <https:////gerrit.fd.io/r/c/vpp/+/36488>`_ [VeC 171]: tests: fix wireguard test failure under heavy load

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 50]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 50]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VeC 50]: nat: fix nat44-ed outside address distribution
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 78]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 84]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 84]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 92]: avf: tolerate socket events in avf_process_request
  | `27972 <https:////gerrit.fd.io/r/c/vpp/+/27972>`_ [VeC 169]: sr: Fix deletion if target SR list is not found
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 169]: api: fix vl_socket_write_ready

**Wayne Morrison** <wmorrison@netgate.com>:

  | `37827 <https:////gerrit.fd.io/r/c/vpp/+/37827>`_ [vEC 2]: vnet: setting rx-mode to adaptive doesn't always have correct effect

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [VEc 19]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 50]: nat: auto forward inbound packet for local server session app with snat
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 55]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 60]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 67]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 68]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 108]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 125]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 126]: cjson: json realloced output truncated if actual lenght more then 256

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 105]: ip: fixup crash when reassemble a lots of fragments.

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37274 <https:////gerrit.fd.io/r/c/vpp/+/37274>`_ [Vec 55]: af_xdp: fix xdp socket create fail

**Yong Liu** <yong.liu@intel.com>:

  | `37821 <https:////gerrit.fd.io/r/c/vpp/+/37821>`_ [VEc 2]: session: map new segment when dma enabled
  | `37823 <https:////gerrit.fd.io/r/c/vpp/+/37823>`_ [vEC 2]: memif: support dma option

**ai hua** <51931196@qq.com>:

  | `37498 <https:////gerrit.fd.io/r/c/vpp/+/37498>`_ [VeC 52]: vppinfra:fix pcap write large file(> 0x80000000) error.

**f00182600** <fangtong2007@163.com>:

  | `36453 <https:////gerrit.fd.io/r/c/vpp/+/36453>`_ [veC 164]: interface: fix the issue of show hardware-interface with invalid if-idx can caused vpp crash.

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 91]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [VEc 30]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 33]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [vEC 18]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 38]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [Vec 50]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 64]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 129]: bonding: Add failover-mac active support

**xujunjie-cover** <xujunjielxx@163.com>:

  | `36494 <https:////gerrit.fd.io/r/c/vpp/+/36494>`_ [VeC 171]: lb: fix make l4 lb function work

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
authors          97
maintainers      36
committers       3
abandoned        0
================ ===

