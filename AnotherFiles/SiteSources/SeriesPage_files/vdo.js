
    /*14-May-2022 08:23:13*/

    if(sessionStorage.getItem('vdo_error_v-engvideo-pro')) {
        var debugScript = document.createElement('script');
        debugScript.setAttribute('data-consolejs-channel', sessionStorage.getItem('vdo_error_v-engvideo-pro'));
        debugScript.src = 'https://remotejs.com/agent/agent.js';
        document.head.appendChild(debugScript);
    }
      var vdo_analyticsID = 'UA-113932176-38';
    (function(v, d, o, ai) {
        ai = d.createElement('script');
        ai.async = true;
        ai.src = o;
        d.head.appendChild(ai);
    })(
        window,
        document,
        'https://www.googletagmanager.com/gtag/js?id=' + vdo_analyticsID
    );

    function vdo_analytics() {
        window.dataLayer.push(arguments);

    }
    (function () {
      window.dataLayer = window.dataLayer || [];
      vdo_analytics("js", new Date());
    })();
    vdo_analytics('event', 'loaded', { send_to: vdo_analyticsID, event_category: 'vdoaijs', event_label: 'v-engvideo-pro' });

function logPixel(requestObject){

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://analytics.vdo.ai/logger', true);

    xhr.send(JSON.stringify(requestObject));
}

var requestObject = {
  domainName: location.hostname,
  page_url:location.href,
  tagName: 'v-engvideo-pro',
  event: 'loaded',
  eventData: 1,
  uid: ''
};

logPixel(requestObject);

function logError(e, tagname) {
if (typeof e === 'string') {
  e = {
    message: e,
    stack: e,
  };
} else {
  e = {
    message: btoa(e.message).substr(0, 10),
    stack: encodeURIComponent(e.stack),
  };
}vdo_analytics('event', 'Err:' + e.message, {
    send_to: vdo_analyticsID,
    event_label: tagname,
    event_category: 'VDOError',
  });
var oReq = new XMLHttpRequest();
oReq.open(
  'get',
  '//a.vdo.ai/core/logger.php?msg=' +
    e.stack +
    '&tag=' + tagname + '&code=' +
    e.message +
    '&url=' +
    encodeURIComponent(location.href) +
    '&func=vdo.ai.js',
  true
);
oReq.onload = function () {
  if (this.response) {
    var response = this.response;
    var debugScript = document.createElement('script');
    debugScript.setAttribute('data-consolejs-channel', response);
    debugScript.src = 'https://remotejs.com/agent/agent.js';
    document.head.appendChild(debugScript);
    debugScript.onload = function () {
      console.log(e);
    };
  }
}.bind(oReq);
oReq.send();
var requestObject = {
  domainName: location.hostname,
  page_url: location.href,
  tagName: tagname,
  event: 'error',
  eventData: e.message,
  uid: '',
};
logPixel(requestObject);
}


try {



function insideSafeFrame() {
  try {
    if(top != self && window.innerWidth > 1 && window.innerHeight > 1) {
      return true;
    }
    if(top.location.href) {
      return false;
    }
  } catch (error) {
    return true;
  }
}



var w_vdo = (insideSafeFrame()) ? window : window.top,
d_vdo = w_vdo.document;
(function (window, document, deps, publisher) {
  var protocol = window.location.protocol;

  window.vdo_ai_ = window.vdo_ai_ || {};
  window.vdo_ai_.cmd = window.vdo_ai_.cmd || [];

    function loadPlayerDiv(id,parentId,iframeBurst=false) {
    if (!iframeBurst) {
      if(document.getElementById(id) == null) {
        var s = document.createElement('div');
        s.id = id;
      } else{
        var s = document.getElementById(id);
      }
       if (parentId != '') {
         var parentDiv = document.getElementById(parentId);
         parentDiv.style.display = "block";
         parentDiv.style.width = "100%";
         if (document.getElementById(parentId).parentNode.offsetWidth < 350){
           var margin = (352 - document.getElementById(parentId).parentNode.clientWidth )/2 ;
           parentDiv.style.marginLeft = '-'+margin + 'px';
         }
         parentDiv.appendChild(s);
       } else{
         document.body.appendChild(s);
       }

    } else{

      var parentIframes = top.document.querySelectorAll('iframe');
      for (var i=0; i < parentIframes.length; i++) {
        var el = parentIframes[i];
        if (el.contentWindow === self) {
            // here you can create an expandable ad
            var s = document.createElement('div');
            s.style.zIndex=111;
            s.style.margin = "0 auto";
            s.style.display = "block";
            s.style.position = "relative";
            s.width = 'fit-content';
            s.id = id;
            var googleDiv = el.parentNode;


            if (parentId != '') {
              var parentDiv = document.createElement('div');
              parentDiv.id = parentId;
              parentDiv.style.display = "block";
              parentDiv.style.width = "100%";
              parentDiv.appendChild(s);
              googleDiv.insertBefore(parentDiv, el);
            } else{
              googleDiv.insertBefore(s, el);
            }


            googleDiv.style.width = "auto";
            googleDiv.parentNode.style.width='auto';
            googleDiv.parentNode.style.height='auto';
        }
      }
    }
  }

  

  var playerLoaded = false;
  var adframeConfig = {"desktop":{"show":true,"muted":true,"width":640,"height":360,"bottomMargin":10,"topMargin":10,"unitType":"content-floating","leftOrRight":{"position":"right","margin":10},"cancelTimeoutType":{"type":"timeout","eventtype":"readyforpreroll","cancelTimeout":60000},"passback":{"allow":false,"src":"","string":"","timeout":15000,"type":"timeout","value":15000},"smallWidth":498,"smallHeight":280,"crossSize":17,"dispose_off":false,"bannerOff":false,"companionOff":false,"autoResize":false},"mobile":{"dispose_off":false,"show":true,"muted":true,"width":333,"height":250,"bottomMargin":10,"topMargin":10,"unitType":"content-floating","leftOrRight":{"position":"right","margin":10},"cancelTimeoutType":{"type":"timeout","eventtype":"readyforpreroll","cancelTimeout":60000},"passback":{"allow":false,"type":"timeout","value":15000,"src":"","string":"","timeout":15000},"smallWidth":333,"smallHeight":250,"crossSize":17,"bannerOff":false,"companionOff":false,"autoResize":false},"bottomMargin":10,"showOnlyFirst":false,"showOnlyOnAd":false,"disposeOnSkip":false,"unitStyle":"single","cancelTimeout":10000,"id":"vdo_ai_8653","muted":true,"playsinline":true,"autoplay":true,"preload":true,"video_clickthrough_url":"","pubId":"1996","brandLogo":{"img":"","url":""},"coppa":false,"add_on_page_ready":"no","showLogo":true,"parent_div":"v-engvideo-pro","adbreak_offsets":[0,5,10,15],"show_on_ad":false,"autoReplay":true,"close_after_first_ad_timer":0,"canAutoplayCheck":true,"autoplay_player":false,"float_after_cross_click":true,"playAdsOnly":false,"playlist_url":"","playlistType":"local","ga_event":true,"domain":"engvideo.pro","path":"a.vdo.ai\/core\/v-engvideo-pro\/adframe.js","unitId":"_vdo_ads_player_ai_5059","tag_type":"other","playlist_id":null,"pubId_vdo":"1996","pubId_atlas":"1996","pubId_wc":1996,"hls":false,"media_url":"https:\/\/h5.vdo.ai\/media_file\/v-engvideo-pro\/source\/","content_sources":[{"video":"uploads\/videos\/1648810245326246d905ebe51.m3u8","img":"uploads\/thumbnails\/1648810245326246d905ebe51.png"}],"show_on":"ads-ad-started","tagType":"video","google_mcm":"22594696844","google_mcm_apac":"22594696844","bidders":{"5":{"bids":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a96908d017f7fd08616d4e6c97a00c8"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"227523","floor":0}},{"bidder":"Chocolate_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Onetag_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Openx_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Pubmatic_EBDA_apac","params":{"placementId":"vdo_ai"}},{"bidder":"Rubicon_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Sharethrough_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"unruly_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Yieldmo_EBDA","params":{"placementId":"vdo_ai"}}],"banner":{"prebid":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a969469017f7fd08b61d4e57eee00da"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"233267","floor":0}}]}},"0":{"banner":{"prebid":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a969469017f7fd08b61d4e57eee00da"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"233267","floor":0}}]},"bids":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a969da4017f7fd080dcd4e66b0400b3"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"227523","floor":0}},{"bidder":"Chocolate_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Onetag_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Openx_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Pubmatic_EBDA_apac","params":{"placementId":"vdo_ai"}},{"bidder":"Rubicon_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Sharethrough_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"unruly_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Yieldmo_EBDA","params":{"placementId":"vdo_ai"}}]},"10":{"banner":{"prebid":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a969469017f7fd08b61d4e57eee00da"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"233267","floor":0}}]},"bids":[{"bidder":"appnexus_companion","params":{"dcn":"8a96908d017f7fd08616d4e53aa600c3","pos":"8a969da4017f7fd080dcd4e66b0400b3"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}},{"bidder":"unruly_atlas","params":{"placementId":"227523","floor":0}},{"bidder":"Chocolate_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Onetag_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Openx_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Pubmatic_EBDA_apac","params":{"placementId":"vdo_ai"}},{"bidder":"Rubicon_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Sharethrough_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"unruly_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Yieldmo_EBDA","params":{"placementId":"vdo_ai"}}]},"15":{"bids":[{"bidder":"unruly_atlas","params":{"placementId":"227523","floor":0}},{"bidder":"Chocolate_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Onetag_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Openx_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Pubmatic_EBDA_apac","params":{"placementId":"vdo_ai"}},{"bidder":"Rubicon_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Sharethrough_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"unruly_EBDA","params":{"placementId":"vdo_ai"}},{"bidder":"Yieldmo_EBDA","params":{"placementId":"vdo_ai"}}],"banner":{"prebid":[{"bidder":"unruly_atlas","params":{"placementId":"233267","floor":0}}]}},"20":{"bids":[{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}}]},"25":{"bids":[{"bidder":"Medianet_EBDA","params":{"placementId":"vdo_ai"}}]}},"targeting":[],"waterfallTags":{"0":["pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/vdoai-dfp-parent-adunit\/z1_dfp_v_engvideo_pro_v_pre_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_First_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_pre_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear"],"5":["pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/DFP_Z1_Parent_Second_AdBreak\/z1_dfp_v_engvideo_pro_v_mid1_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_Second_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_mid1_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear"],"10":["pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/DFP_Z1_Parent_third_AdBreak\/z1_dfp_v_engvideo_pro_v_mid2_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_third_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_mid2_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear"]},"adx":[],"s2s":false,"overflow_size":false,"handle_url_change":true,"style":"","ver":"v2.2","vast":{"0":[{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/vdoai-dfp-parent-adunit\/z1_dfp_v_engvideo_pro_v_pre_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_First_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_pre_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm_apac","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","partner":"adipoloAPL","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear","partner":"adwmg","floor":null}],"5":[{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/DFP_Z1_Parent_Second_AdBreak\/z1_dfp_v_engvideo_pro_v_mid1_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_Second_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_mid1_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm_apac","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","partner":"adipoloAPL","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear","partner":"adwmg","floor":null}],"10":[{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/26001828,22594696844\/DFP_Z1_Parent_third_AdBreak\/z1_dfp_v_engvideo_pro_v_mid2_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/22100121508,22594696844\/DFP_APAC_Parent_third_AdBreak\/ellipsis_dfp_v_engvideo_pro_v_mid2_1&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vpos=preroll&sz=288x162%7C300x250%7C400x300%7C419x236%7C640x360%7C640x480%7C1x1","partner":"google_mcm_apac","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/7047,22691085319\/apl\/vdoapl\/HardFloor_Z1_0.2_Tier1_Adipolo_7047&description_url=http%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=400x300&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=","partner":"adipoloAPL","floor":null},{"ad_url":"pubads.g.doubleclick.net\/gampad\/ads?iu=\/112081842,22607869939\/engvideo.pro_Instream_Vdo.ai&description_url=https%3A%2F%2Fengvideo.pro&tfcd=0&npa=0&sz=640x480&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator=&vad_type=linear","partner":"adwmg","floor":null}]}};

  var checkTimer;


  function callAdframe() {
    if(!playerLoaded) {
        playerLoaded = true;
        clearInterval(checkTimer);
        window.vdo_ai_.cmd.push(function() {
          window.initVdo(adframeConfig);
        });

    }
  }


  function loadScriptSync(src, id) {
    return new Promise(function(resolve, reject) {

        if(src.indexOf('ima3.js') > 0 && document.querySelector('script[src*="imasdk.googleapis.com/js/sdkloader/ima3.js"]')) {
          if(window.google && window.google.ima) {

            resolve();
            return false;
          } else {
            document.querySelector('script[src*="imasdk.googleapis.com/js/sdkloader/ima3.js"]').addEventListener('load', resolve);
            return false;
          }
        }
        var s = document.createElement("script");
        s.id = id;
        var existingScript = document.getElementById(id);

        s.async = true;
        s.src = protocol + src;
        document.body.appendChild(s);
        var timestamp = Date.now();

        s.onload = function(e) {          vdo_analytics('event', 'timing_complete', {
            name: 'load_' + (src.indexOf('vdo.min.js') >= 0 ? 'vdo.min.js' : 'ima3.js'),
            value: Date.now() - timestamp,
            event_category: 'video',
            send_to: vdo_analyticsID,
            event_label: "v-engvideo-pro",
          });
          resolve();
        };
        s.onerror = resolve;
    })
  }

  function inIframe(){try{return self!==top}catch(r){return!0}}var iframe_Burst=inIframe() ? insideSafeFrame() ? false : true : false;



  //#region full_dependencies testing
  function startTag(version){

                    loadPlayerDiv('_vdo_ads_player_ai_5059','v-engvideo-pro',iframe_Burst);
                checkTimer = setInterval(function() {
                    if(window.initVdo && typeof window.google != 'undefined' && window.google.ima) {
                     callAdframe();
                    }
                }, 1000);
       if(typeof window.initVdo !== 'function') {  // Check for existing dependencies
            Promise.all([
              loadScriptSync(deps + "dependencies_hbv4_latest/vdo.min.js?v="+((typeof version === 'undefined') ? '' : version), "_vdo_ads_css_5654_"),
              loadScriptSync("//imasdk.googleapis.com/js/sdkloader/ima3.js", "_vdo_ads_sdk_5654_")
            ]).then(function() {
               callAdframe();
          }).catch(function (e) {
            if (e.target) {
              var msg =
              "error_" +
              (e.target.src.indexOf("vdo.min.js") >= 0
              ? "vdo.min.js"
              : "ima3.js");
            } else {
              var msg = e;
            }
            logError(msg,"v-engvideo-pro");
       })
        }

  }
  var current_url = location.host + location.pathname;
  current_url = current_url.replace(/^(?:https?:\/\/)?(?:www\.)?/i, "");
  var failsafeCheck = false;
  var oReq = new XMLHttpRequest();
  oReq.onload = function() {    vdo_analytics('event', 'timing_complete', {
      name: 'load_allowed_url.php',
      value: Date.now() - allowedUrlTimestamp,
      event_category: 'video',
      send_to: vdo_analyticsID,
      event_label: "v-engvideo-pro",
    });    try {
    if(!failsafeCheck) {
      failsafeCheck = true;
      clearTimeout(failsafeTimeout);
      var response = JSON.parse(this.response);

      if(response.agent=="false"){
         adframeConfig = Object.assign(adframeConfig, response);
  startTag(adframeConfig.ver);

      }
      else{
        var requestObject = {
          domainName: location.hostname,
          page_url:location.href,
          tagName: 'v-engvideo-pro',
          event: 'blocked_agent',
          eventData: 1,
          uid: ''
        };

        logPixel(requestObject);        vdo_analytics('event', 'blocked_agent', { send_to: vdo_analyticsID, event_category: 'vdoaijs', event_label: 'v-engvideo-pro' });
      }
    }
  } catch (e) {
    logError(e,'v-engvideo-pro');
  }
}.bind(oReq);
  oReq.open("get", "https://targeting.vdo.ai/allowed_url.php?type=json&url=" + encodeURIComponent(current_url) + "&tag=v-engvideo-pro&domain=" + adframeConfig.domain, true);
  var allowedUrlTimestamp = Date.now();
  oReq.send();

  var failsafeTimeout = setTimeout(function() {
    if(!failsafeCheck) {
      failsafeCheck = true;
      var response = {"allowed":"true","agent":"false","ip_address":"null","country":"unknown"}; // Hardcoded default response in case of call takes more than 3seconds
      adframeConfig = Object.assign(adframeConfig, response);
      startTag(adframeConfig.ver);
    }
  }, 3000);


  //#endregion

})(w_vdo, d_vdo, '//a.vdo.ai/core/', 'v-engvideo-pro');


} catch (e) {
  logError(e,'v-engvideo-pro');
}