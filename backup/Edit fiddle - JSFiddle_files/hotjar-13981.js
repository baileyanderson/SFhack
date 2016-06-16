window.hjSiteSettings = window.hjSiteSettings || {"testers_widgets":[],"surveys":[],"heatmaps":[],"recording_capture_keystrokes":true,"polls":[{"persist_condition":"response","targeting":[{"negate":false,"pattern":"jsfiddle.net","match_operation":"contains","component":"url"},{"negate":false,"pattern":"desktop","match_operation":"exact","component":"device"}],"language":"en","targeting_percentage":100,"created_epoch_time":1465970578,"display_condition":"delay","content":{"thankyou":"Thank you for answering this Poll. Your feedback is highly appreciated!","questions":[{"nextByAnswer":[],"text":"Would you prefer having full control over HTML (DOCTYPE, BODY, HEAD, META, LINK tags) in the HTML panel or just the snippet without these tags?","labels":null,"answers":[{"text":"Just snippet","comments":false},{"text":"Whole HTML","comments":false}],"next":"byOrder","type":"single-close-ended","randomize_answer_order":true}]},"effective_show_branding":true,"background":"#262E3D","skin":"dark","position":"left","display_delay":5,"id":53700}],"site_id":13981,"record_targeting_rules":[],"forms":[],"record":false,"r":0.0477281405,"deferred_page_contents":[]};

window.hjBootstrap = window.hjBootstrap || function (scriptUrl) {
    var s = document.createElement('script');
    s.src = scriptUrl;
    document.getElementsByTagName('head')[0].appendChild(s);
    window.hjBootstrap = function() {};
};

hjBootstrap('https://script.hotjar.com/modules-e12a7ede294d22ffa3a8a711155156e3.js');