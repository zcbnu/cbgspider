!function(e) {
    if ("function" == typeof define && window.define.amd)
        window.define([], e);
    else
        e()
}(function() {
    var e = "2020-09-20";
    var t = "";
    var i = "IS_NOTNEW_MSG";
    window.URSCFG = {};
    window.URSOPENBGP = "{URSOPENBGPVALUE}";
    var n = {}
      , o = {}
      , r = {}
      , s = {}
      , a = []
      , c = 0;
    if (!Function.prototype.bind)
        Function.prototype.bind = function(e) {
            if ("function" != typeof this)
                throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");
            var t = Array.prototype.slice.call(arguments, 1)
              , i = this
              , n = function() {}
              , o = function() {
                return i.apply(this instanceof n && e ? this : e, t.concat(Array.prototype.slice.call(arguments)))
            };
            if (this.prototype)
                n.prototype = this.prototype;
            o.prototype = new n;
            return o
        }
        ;
    var l = function(e) {
        var t = document.createElement("img");
        t.style.position = "absolute";
        t.style.width = "0px";
        t.style.height = "0px";
        document.body.appendChild(t);
        t.src = e;
        setTimeout(function() {
            document.body.appendChild(t)
        }, 1e4)
    };
    var f = function(e) {
        var t = e.time || 0;
        if (100 * Math.random() <= 1)
            h.call(this, "renderOk", t)
    };
    var u = [1e3, 1200, 3e3, 5e3, 1e4, 15e3, 2e4, 25e3, 3e4];
    var d = function(e) {
        var t = (new Date).getTime();
        if (e)
            t = parseInt(e, 10);
        var i = t - this.webzjStartTime || 0;
        var n = 1;
        for (var o = u.length - 1; o >= 0; o--)
            if (i > u[o]) {
                n = o + 2;
                break
            }
        return n
    };
    var h = function(e, t) {
        try {
            var i = d.call(this, t);
            var n = this._url_cache.split("//")[1].split("/")[0];
            var o = "https://pr.nss.netease.com/sentry/passive?clusterName=urs-webzj-static-passive&modelName=webzj_response_time2&one=1&pd=" + this._urs_options.product + "&pkid=" + this._urs_options.promark + "&uapi=" + e + "&dataTime=" + (new Date).getTime() + "&domain=" + n;
            for (var r = 1; r <= 10; r++)
                if (i === r)
                    o = o + "&step" + r + "=1";
                else
                    o = o + "&step" + r + "=0";
            l(o)
        } catch (s) {}
    };
    var p = function(e) {
        return e.replace(/\/\/([^\/]+:?)\//, function(e, t) {
            var i = t;
            i = i.replace(/([^\.]+:?)\./, function(e, t) {
                return t + "-v6."
            });
            return "//" + i + "/"
        })
    };
    var g = function(e) {
        e = parseInt(e, 10);
        return e >= 3
    };
    var m = function() {
        var e = navigator.userAgent.toLowerCase();
        var t = /msie/.test(e) && !/opera/.test(e);
        var i = (e.match(/.+(?:rv|it|ra|ie)[\/: ]([\d.]+)/) || [0, "0"])[1];
        var n = {
            6: "2.0",
            7: "3.0",
            8: "4.0",
            9: "5.0",
            10: "6.0",
            11: "7.0"
        };
        var o = n[document.documentMode] || n[parseInt(i)];
        if (t && parseInt(o, 10) < 4 && !window.postMessage)
            return 1;
        else
            return 0
    };
    var v = function(e, t, i) {
        if (window.addEventListener)
            e.addEventListener(t, i, !1);
        else
            e.attachEvent("on" + t, i)
    };
    var w = function(e, t, i) {
        if (window.removeEventListener)
            e.removeEventListener(t, i);
        else
            e.detachEvent("on" + t, i)
    };
    var _ = function(e) {
        e = e || "";
        if ((e.indexOf("passport.") >= 0 || e.indexOf("dl.reg.163.com") >= 0 || e.indexOf("reg.icourse163.org") >= 0) && e.indexOf("/webzj") >= 0)
            e = e.replace(/\:\/\/[^\/]+\/webzj\//, function(e) {
                return e + "b/"
            });
        else
            e = e.replace(/\:\/\/([^\/]+)/, function(e) {
                return e + "/b"
            });
        return e
    };
    var b = [];
    var y = function(e) {
        var t = "";
        var i = r[e];
        if (i.__coverBackground && D("animation"))
            t = i.__coverBackground.indexOf("background:") != -1 ? i.__coverBackground : "";
        return "position:fixed;_position:absolute;top:0;left:0;width:100%;height:100%;overflow:hidden;background:rgb(0,0,0); filter:progid:DXImageTransform.Microsoft.Alpha(opacity=60);-moz-opacity:0.6;-khtml-opacity:0.6;opacity:0.6;z-index:1000;" + t
    };
    var S = function(e, t) {
        return "position:fixed;_position:absolute;z-index:10000;left:50%;top:50%;width:" + e + "px;margin-left:-" + e / 2 + "px;height:" + t + "px;margin-top:-" + t / 2 + "px;"
    };
    var I = function(e) {
        var t = r[e];
        var i = null;
        if (t.__iframeShowAnimation)
            i = "-webkit-animation:" + t.__iframeShowAnimation + ";-moz-animation:" + t.__iframeShowAnimation + ";-ms-animation:" + t.__iframeShowAnimation + ";-o-animation:" + t.__iframeShowAnimation + ";animation:" + t.__iframeShowAnimation + ";";
        return "width:100%;height:100%;border:none;background:none;" + (i ? i : "")
    };
    var M = function() {
        var e = setInterval(function() {
            for (var t = 0; t < a.length; t++)
                if (a[t].readyDone) {
                    e = clearInterval(e);
                    a.shift();
                    k(1);
                    break
                }
        }, 200)
    };
    var k = function(e) {
        if (e || !c) {
            c = 1;
            var t = setInterval(function() {
                for (var e = 0; e < a.length; e++)
                    if (!a[e].readyDone) {
                        t = clearInterval(t);
                        x.call(a[e]);
                        M();
                        break
                    }
            }, 200)
        }
    };
    var U = function(e, t, i) {
        var n = i.id;
        var o = "x-URS-iframe" + n;
        var s = r[n];
        var c = document.getElementById(o)
          , l = s._name || "";
        if (!c) {
            try {
                c = document.createElement('<iframe  name="' + l + '" allowTransparency=true ></iframe>')
            } catch (f) {
                c = document.createElement("iframe");
                c.allowTransparency = !0;
                c.name = l
            }
            c.frameBorder = 0;
            c.id = o;
            c.scrolling = "no";
            c.style.cssText = I(n)
        }
        if (t)
            e.appendChild(c);
        else {
            var u = 420
              , d = 408;
            if (s.frameSize) {
                u = s.frameSize.width;
                d = s.frameSize.height
            }
            var h = document.getElementById("x-discover" + n);
            if (!h) {
                h = document.createElement("div");
                h.id = "x-discover" + n;
                h.style.cssText = y(n)
            }
            var p = document.getElementById("x-panel" + n);
            if (!p) {
                p = document.createElement("div");
                p.id = "x-panel" + n;
                s._panel = p;
                p.style.cssText = S(u, d)
            }
            p.appendChild(c);
            e.appendChild(h);
            e.appendChild(p);
            e.style.display = "none"
        }
        if (!window.postMessage) {
            a.push(this);
            k(0)
        }
    };
    var C = function() {
        var e = window.URSCFG[this.MGID];
        this._url_cache = this._url_cache.replace("webzj.reg.163.com", "webzj2.reg.163.com");
        if (e._$passportNeedUrsBgp)
            if ("is_IPV6_Message" === t && this._url_cache.indexOf("-v6") !== -1)
                this._url_cache = this._url_cache.replace("passport-v6.", "passport2.").replace("reg-v6.icourse163.org", "reg2.icourse163.org").replace("dl-v6.reg.163.com", "dl2.reg.163.com").replace("/v6/", "/v1.0.1/");
            else
                this._url_cache = this._url_cache.replace("passport.", "passport2.").replace("reg.icourse163.org", "reg2.icourse163.org").replace("dl.reg.163.com", "dl2.reg.163.com");
        if (this._urs_options.wdaId)
            this._url_cache = this._url_cache.replace(/wdaId=([^&]+)/, "wdaId=UA1482833332087")
    };
    var R = function(e) {
        var i = "x-URS-iframe" + this.MGID;
        var n = document.getElementById(i);
        if (this._urs_options && this._urs_options.afterSetIframeSrc)
            this._urs_options.afterSetIframeSrc(n);
        if ("{URSOPENBGPVALUE}" != window.URSOPENBGP)
            C.call(this);
        window.setTimeout(function() {
            this.__loadTime = (new Date).getTime();
            if (n) {
                if ("is_IPV6_Message" === t)
                    if (e != -1 && 1 != e && "{URSOPENBGPVALUE}" === window.URSOPENBGP)
                        this._url_cache = p(this._url_cache);
                n.src = this._url_cache
            }
        }
        .bind(this), 0);
        if (e !== -1) {
            this.sto = clearTimeout(this.sto);
            var o = window.URSCFG[this.MGID];
            if (o._$needUrsBgp && "{URSOPENBGPVALUE}" === window.URSOPENBGP)
                if (1 != e) {
                    this.sto = setTimeout(function() {
                        this.sto = clearTimeout(this.sto);
                        h.call(this, "bgp");
                        this.webzjStartTime = (new Date).getTime();
                        C.call(this);
                        R.call(this, 1)
                    }
                    .bind(this), this._urs_options.bgpTime);
                    return
                }
            this.sto = setTimeout(function() {
                try {
                    if (this._urs_options.loadTimeout)
                        this._urs_options.loadTimeout()
                } catch (e) {}
                h.call(this, "help");
                this.sto = clearTimeout(this.sto);
                var t = location.href || "";
                t = t.substring(0, 200);
                var i = (new Date).getTime() + Math.random();
                var n;
                try {
                    n = this._url_cache.split("//")[1].split("/")[0]
                } catch (e) {}
                var o = E({
                    pkid: this._urs_options.promark,
                    pd: this._urs_options.product,
                    time: i,
                    from: t,
                    domain: n
                }, "&", !0);
                this._url_cache = "//hc.reg.163.com/webcomponent/guide.html?" + o;
                R.call(this, -1)
            }
            .bind(this), 2e4)
        }
    };
    var D = function(e) {
        var t = ["webkit", "Moz", "ms", "o"], i, n = [], o = document.documentElement.style, r = function(e) {
            return e.replace(/-(\w)/g, function(e, t) {
                return t.toUpperCase()
            })
        };
        for (i in t)
            n.push(r(t[i] + "-" + e));
        n.push(r(e));
        for (i in n)
            if (n[i]in o)
                return !0;
        return !1
    };
    var T = function(e, i) {
        var n = document.getElementById("x-URS-iframe" + e);
        var o = window.name || "_parent";
        var r = {};
        r.data = i;
        r.data.from = "URS|";
        r.data.topURL = location.href || "";
        r.origin = "*";
        r.source = o;
        if ("is_IPV6_Message" === t)
            r.data.mv = "new_cdn_101_v6";
        else
            r.data.mv = "new_cdn_101";
        r.data.loadTime = (new Date).getTime() - this.__loadTime;
        if (n)
            G(n.contentWindow, r)
    };
    var x = function() {
        T.call(this, this.MGID, this._urs_options)
    };
    var O = function() {
        var e = /^([\w]+?:\/\/.*?(?=\/|$))/i;
        return function(t) {
            t = t || "";
            if (e.test(t))
                return RegExp.$1;
            else
                return "*"
        }
    }();
    var j = function(e, t) {
        try {
            t = t.toLowerCase();
            if (null === e)
                return "null" == t;
            if (void 0 === e)
                return "undefined" == t;
            else
                return Object.prototype.toString.call(e).toLowerCase() == "[object " + t + "]"
        } catch (i) {
            return !1
        }
    };
    var E = function(e, t, i) {
        if (!e)
            return "";
        var n = [];
        for (var o in e)
            if (e.hasOwnProperty(o)) {
                var r = e[o];
                if (r)
                    if (!j(r, "function")) {
                        if (j(r, "date"))
                            r = r.getTime();
                        else if (j(r, "array"))
                            r = r.join(",");
                        else if (j(r, "object"))
                            r = JSON.stringify(r);
                        if (i)
                            r = encodeURIComponent(r);
                        n.push(encodeURIComponent(o) + "=" + r)
                    } else
                        ;
                else
                    ;
            } else
                ;
        return n.join(t || ",")
    };
    var G = function() {
        var e = "MSG|";
        var t = function(t) {
            var i = {};
            t = t || {};
            i.origin = t.origin || "";
            i.ref = location.href;
            i.self = t.source;
            i.data = JSON.stringify(t.data);
            return e + E(i, "|", !0)
        };
        return function(e, i) {
            if (window.postMessage) {
                i = i || {};
                e.postMessage(JSON.stringify(i.data), O(i.origin))
            } else
                b.unshift({
                    w: e,
                    d: escape(t(i))
                })
        }
    }();
    var B = function() {
        var e = navigator.appName;
        if ("Netscape" == e) {
            var t = window.open("about:blank", "_self");
            t.opener = null;
            t.close()
        } else if ("Microsoft Internet Explorer" == e) {
            window.opener = null;
            window.open("", "_self");
            window.close()
        }
    };
    var P = function(e, i) {
        var n;
        var o = 0 != e.isHttps ? "https://" : "http://";
        if (e.cssDomain && e.cssFiles)
            if (e.cssDomain.indexOf("http://") != -1)
                o = "http://";
        if (g(e.version)) {
            n = "index2.html";
            if (e.single) {
                n = "index_dl2.html";
                if ("register" == e.page)
                    n = "index_reg2.html"
            }
        } else {
            n = "index.html";
            if (e.single) {
                n = "index_dl.html";
                if ("register" == e.page)
                    n = "index_reg.html"
            }
        }
        if ("1" == e.newCDN)
            n = n.replace(".html", "_new.html");
        var r;
        if ("is_IPV6_Message" === t)
            r = e.crossDomainUrl || "webzj.reg.163.com/v6/pub/";
        else
            r = e.crossDomainUrl || "webzj.reg.163.com/v1.0.1/pub/";
        this._url_cache = o + r + n;
        if (e.isDevDemo)
            this._url_cache = o + "dl.reg.163.com/webapp/html/" + n;
        var s = parseInt(1e3 * Math.random());
        e.pathB = 0;
        var a = window.URSCFG[e.promark];
        if (a)
            if (s <= a)
                e.pathB = 1;
        if (e.pathB)
            this._url_cache = _(this._url_cache);
        if (i.__cssStr)
            this._url_cache += "?" + i.__cssStr + "&MGID=" + this.MGID + "&wdaId=" + (e.wdaId || "");
        else
            this._url_cache += "?MGID=" + this.MGID + "&wdaId=" + (e.wdaId || "");
        this._urs_options = e || {};
        this._urs_options.bgpTime = e.bgpTime || 1e4;
        this._url_cache += "&pkid=" + (this._urs_options.promark || "") + "&product=" + (this._urs_options.product || "");
        if (e.cdnhostname)
            this._url_cache += "&cdnhostname=" + e.cdnhostname;
        return this._url_cache
    };
    window.URS = function() {
        var e = function() {
            var t = (new Date).getTime() + Math.random();
            if (!s[t]) {
                s[t] = t;
                return t
            } else
                return e()
        };
        var a = function(e) {
            var i = e.cookieDomain || "";
            var n = e.regCookieDomain || "";
            var o = e.crossDomainUrl || "";
            var r, s;
            if (!o) {
                if (i) {
                    e.regCookieDomain = i;
                    r = i
                } else if (n) {
                    e.cookieDomain = n;
                    r = n
                }
                if ("is_IPV6_Message" === t)
                    s = "v6";
                else
                    s = "v1.0.1";
                if (r)
                    if (r.indexOf("icourse163") > -1)
                        e.crossDomainUrl = "reg." + r + "/webzj/" + s + "/pub/";
                    else
                        e.crossDomainUrl = "passport." + r + "/webzj/" + s + "/pub/";
                else
                    e.crossDomainUrl = "dl.reg.163.com/webzj/" + s + "/pub/"
            }
            return e
        };
        var c = function(n) {
            this.MGID = e();
            window.URSCFG[this.MGID] = {};
            var o = window.URSCFG[this.MGID];
            n.from3Cdn = 1;
            if ("IS_NEW_MSG" === i) {
                n.newCDN = 1;
                if (!n.cdnhostname)
                    n.cdnhostname = "is_IPV6_Message" === t ? "webzj-v6.netstatic.net" : "webzj.netstatic.net"
            }
            if (n.from3Cdn && g(n.version))
                n = a.call(this, n);
            if (m())
                n.needUrsBgp = 0;
            if ("0" == n.needUrsBgp) {
                n.passportNeedUrsBgp = 0;
                o._$needUrsBgp = 0;
                o._$passportNeedUrsBgp = 0
            } else {
                if (n.crossDomainUrl || n.cookieDomain) {
                    o._$passportNeedUrsBgp = 1;
                    n.passportNeedUrsBgp = 1
                }
                o._$needUrsBgp = 1;
                n.needUrsBgp = 1
            }
            r[this.MGID] = {};
            this._$COM_NUM = 1 == this._$COM_NUM ? 1 : 2;
            var s = r[this.MGID];
            s.promark = n.promark;
            s.frameSize = n.frameSize;
            s.__coverBackground = n.coverBackground;
            s.__iframeShowAnimation = n.iframeShowAnimation;
            if (n.cssDomain && n.cssFiles)
                s.__cssStr = "cd=" + encodeURIComponent(n.cssDomain) + "&cf=" + encodeURIComponent(n.cssFiles);
            this.isInclude = 0;
            if (n.includeBox)
                if ("string" == typeof n.includeBox)
                    this.isInclude = document.getElementById(n.includeBox) || 0;
                else
                    this.isInclude = n.includeBox;
            s.needPrepare = n.needPrepare || 0;
            if ("string" == typeof n.eventType)
                this._type = n.eventType;
            if ("string" == typeof n.bid)
                this._btn = document.getElementById(n.bid);
            else
                this._btn = n.bid;
            if (n.doPwdFocus)
                this.doPwdFocus = n.doPwdFocus;
            if (n.doPwdHide)
                this.doPwdHide = n.doPwdHide;
            if (n.logincb)
                this.logincb = n.logincb;
            if (n.closecb)
                this.closecb = n.closecb;
            if (n.regcb)
                this.regcb = n.regcb;
            if (n.loginCheckLock)
                this.loginCheckLock = n.loginCheckLock;
            if (n.regCheckLock)
                this.regCheckLock = n.regCheckLock;
            if (n.initReady)
                this.initReady = n.initReady;
            if (n.statecb)
                this.statecb = n.statecb;
            if (n.resize)
                this.resize = n.resize;
            if (n.changepage)
                this.changepage = n.changepage;
            if (n.moduleResize)
                this.moduleResize = n.moduleResize;
            if (n.loginstate)
                this.loginstate = n.loginstate;
            if (n.otherRegSuccess)
                this.otherRegSuccess = n.otherRegSuccess;
            if (n.lockMbLoginState)
                this.lockMbLoginState = n.lockMbLoginState;
            if (n.lockMbRegState)
                this.lockMbRegState = n.lockMbRegState;
            if (n.mbInitSuccess)
                this.mbInitSuccess = n.mbInitSuccess;
            if (n.mbChangeModule)
                this.mbChangeModule = n.mbChangeModule;
            if (n.loginInitSuccess)
                this.loginInitSuccess = n.loginInitSuccess;
            if (n.regInitSuccess)
                this.regInitSuccess = n.regInitSuccess;
            if (n.renderOk)
                this.renderOk = n.renderOk;
            if (n.WeiXinInputBlur)
                this.WeiXinInputBlur = n.WeiXinInputBlur;
            if (n.loginEmailValue)
                this.loginEmailValue = n.loginEmailValue;
            if (n.loginMbValue)
                this.loginMbValue = n.loginMbValue;
            if (n.InputBlur)
                this.InputBlur = n.InputBlur;
            if (n.sendSmsOk)
                this.sendSmsOk = n.sendSmsOk;
            var c = document.createElement("div");
            c.id = "x-URS" + this.MGID;
            document.body.appendChild(c);
            this.box = c;
            this._url_cache = P.call(this, n, s);
            try {
                JSON.stringify(this._urs_options)
            } catch (l) {
                return null
            }
            if (!this.isInclude) {
                if (this._btn && this._type)
                    v(this._btn, this._type, this.showIframe.bind(this))
            } else
                this.includeBox = this.isInclude
        };
        var l = function(e) {
            if (e)
                e.stopPropagation ? e.stopPropagation() : e.cancelBubble = !0
        };
        var u = function(e) {
            l(e);
            var t = e.data || "{}";
            if ("string" == typeof t)
                try {
                    t = JSON.parse(t)
                } catch (i) {
                    t = {}
                }
            if (n[t.MGID])
                n[t.MGID]({
                    data: t,
                    origin: O(e.origin)
                })
        };
        var d = function(e) {
            var t = e.data, i, n, s;
            if (t) {
                if ("string" == typeof t)
                    try {
                        t = JSON.parse(t)
                    } catch (a) {
                        t = {}
                    }
                if (t.MGID) {
                    i = o[t.MGID];
                    n = r[t.MGID];
                    if (i.isInclude)
                        s = i.includeBox;
                    else
                        s = n._panel;
                    if (t["URS-READY-DONE"]) {
                        i.readyDone = 1;
                        i.sto = clearTimeout(i.sto);
                        if (i.initReady)
                            i.initReady()
                    }
                    if (t["URS-READY"]) {
                        i.sto = clearTimeout(i.sto);
                        i.ursReady = 1
                    }
                    if (!window.postMessage || !t["URS-READY"] || !i.isInclude && n.needPrepare) {
                        if (t["URS-READY"] && !n._initReady)
                            n._initReady = !0;
                        if (!t["URS-CM-STATE"])
                            if (!t || !t.fromOutLogin || t.toOpener) {
                                if ("sendSmsOk" === t.type) {
                                    if (i.sendSmsOk)
                                        i.sendSmsOk(t)
                                } else if ("InputBlur" === t.type) {
                                    if (i.InputBlur)
                                        i.InputBlur()
                                } else if ("loginEmailValue" === t.type) {
                                    if (i.loginEmailValue)
                                        i.loginEmailValue(t)
                                } else if ("loginMbValue" === t.type) {
                                    if (i.loginMbValue)
                                        i.loginMbValue(t)
                                } else if ("WeiXinInputBlur" === t.type) {
                                    if (i.WeiXinInputBlur)
                                        i.WeiXinInputBlur()
                                } else if ("renderOk" == t.type) {
                                    if (i.renderOk)
                                        i.renderOk(t);
                                    f.call(this, t)
                                } else if ("moduleResize" == t.type) {
                                    if (i.moduleResize)
                                        i.moduleResize(t)
                                } else if ("regInitSuccess" == t.type) {
                                    if (i.regInitSuccess)
                                        i.regInitSuccess()
                                } else if ("loginInitSuccess" == t.type) {
                                    if (i.loginInitSuccess)
                                        i.loginInitSuccess()
                                } else if ("mbChangeModule" == t.type) {
                                    if (i.mbChangeModule)
                                        i.mbChangeModule()
                                } else if ("mbInitSuccess" == t.type) {
                                    if (i.mbInitSuccess)
                                        i.mbInitSuccess()
                                } else if ("lockMbLoginState" == t.type) {
                                    if (i.lockMbLoginState)
                                        i.lockMbLoginState(t)
                                } else if ("lockMbRegState" == t.type) {
                                    if (i.lockMbRegState)
                                        i.lockMbRegState(t)
                                } else if ("otherRegSuccess" == t.type) {
                                    if (i.otherRegSuccess)
                                        i.otherRegSuccess(t)
                                } else if ("success" == t.type) {
                                    if (i.logincb)
                                        i.logincb(t["username"], t["isOther"], t);
                                    if (!this.isInclude) {
                                        if (i._btn && i._type)
                                            w(i._btn, i._type, i.showIframe.bind(i));
                                        i.closeIframe()
                                    }
                                } else if ("close" == t.type) {
                                    if (i.closecb)
                                        i.closecb();
                                    i.closeIframe()
                                } else if ("resize" == t.type || "init" == t.type) {
                                    s.style.width = t.width + "px";
                                    s.style.height = t.height + "px";
                                    if (!i.isInclude)
                                        s.style.marginLeft = -1 * t.width / 2 + "px";
                                    if (i.resize)
                                        i.resize(t)
                                } else if ("register-success" == t.type) {
                                    if (i.regcb)
                                        i.regcb(t["username"], t["url"])
                                } else if ("lockLoginState" == t.type) {
                                    if (i.loginCheckLock)
                                        i.loginCheckLock(t.value)
                                } else if ("lockRegState" == t.type) {
                                    if (i.regCheckLock)
                                        i.regCheckLock(t.value)
                                } else if ("changepage" == t.type) {
                                    if (i.changepage)
                                        i.changepage(t.page)
                                } else if ("loginstate" == t.type) {
                                    if (i.loginstate)
                                        i.loginstate(t)
                                } else if ("doPwdFocus" == t.type) {
                                    try {
                                        setTimeout(function() {
                                            var e = document.getElementById("x-URS-iframe" + i.MGID);
                                            if (e) {
                                                var n = e.offsetTop;
                                                var o = e.offsetLeft
                                            }
                                            window.scrollTo(t.offset.x + o, t.offset.y + n)
                                        }, 200)
                                    } catch (a) {}
                                    if (i.doPwdFocus)
                                        i.doPwdFocus(t)
                                } else if ("doPwdHide" == t.type)
                                    if (i.doPwdHide)
                                        i.doPwdHide(t)
                            } else {
                                try {
                                    window.opener.$outLogin(t)
                                } catch (a) {}
                                setTimeout(function() {
                                    B()
                                }, 200)
                            }
                        else if (i.statecb)
                            i.statecb(t["URS-CM-STATENAME"], t["URS-CM-STATE"])
                    } else
                        x.call(i)
                }
            }
        };
        var h = function() {
            var e = "MSG|";
            var t = function(e, t) {
                var i = j(t, "function") ? t : function(e) {
                    return e === t
                }
                  , n = null;
                for (var o = 0, r = e.length - 1, s; o < r; o++) {
                    s = e[o];
                    if (i(s))
                        n = o
                }
                return null != n ? n : -1
            };
            var i = function() {
                var e;
                var i = function(i, n, o) {
                    if (t(e, i.w) < 0) {
                        e.push(i.w);
                        o.splice(n, 1);
                        i.w.name = i.d
                    }
                };
                return function() {
                    e = [];
                    if (b && b.length)
                        for (var t = b.length, n; t--; t >= 0) {
                            n = b[t];
                            i(n, t, b)
                        }
                    e = null
                }
            }();
            var n = function() {
                var t = unescape(window.name || "");
                if (t && 0 == t.indexOf(e)) {
                    window.name = "";
                    var i = t.replace(e, "")
                      , n = i.split("|")
                      , o = n.length
                      , r = {};
                    for (var s = 0; s < o; s++) {
                        var a = n[s].split("=");
                        if (!a || !a.length)
                            return;
                        var c = a.shift();
                        if (!c)
                            return;
                        r[decodeURIComponent(c)] = decodeURIComponent(a.join("="))
                    }
                    i = r;
                    var l = (i.origin || "").toLowerCase();
                    if (!l || "*" == l || 0 == location.href.toLowerCase().indexOf(l))
                        d({
                            data: i.data || "null",
                            origin: O(i.ref || document.referrer)
                        })
                }
            };
            return function() {
                setInterval(i, 100);
                setInterval(n, 20)
            }
        }();
        var p = function() {
            if (!window.__hasRun) {
                if (window.postMessage)
                    v(window, "message", u);
                else
                    h();
                window.__hasRun = 1
            }
        };
        return function(e) {
            this.webzjStartTime = (new Date).getTime();
            c.call(this, e);
            var t = r[this.MGID];
            if (t.needPrepare || this.isInclude)
                this.prepareIframe();
            n[this.MGID] = d.bind(this);
            o[this.MGID] = this;
            return p()
        }
    }();
    window.URS.prototype.safekeyboardMsg = function(e) {
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.prepareIframe = function() {
        if (this.isInclude) {
            U.call(this, this.includeBox, 1, {
                id: this.MGID
            });
            R.call(this);
            this.showIframe()
        } else {
            U.call(this, this.box, 0, {
                id: this.MGID
            });
            R.call(this)
        }
    }
    ;
    window.URS.prototype.showIframe = function(e) {
        var t = r[this.MGID];
        if (!this.isInclude)
            if (!t.needPrepare) {
                U.call(this, this.box, 0, {
                    id: this.MGID
                });
                R.call(this)
            } else if (!t._initReady)
                return;
        e = e || {};
        if (e.page) {
            if (100 * Math.random() <= 1)
                try {
                    var i = "//webzj-v6.reg.163.com/UA1435545636633/__utm.gif?log=usepage&pd=" + this._urs_options.product || "";
                    var n = document.createElement("img");
                    n.style.position = "absolute";
                    n.style.width = "0px";
                    n.style.height = "0px";
                    document.body.appendChild(n);
                    n.src = i;
                    setTimeout(function() {
                        document.body.appendChild(n)
                    }, 1e4)
                } catch (o) {}
            if (e.page != this._urs_options.page && this._urs_options.single) {
                this._urs_options.page = e.page;
                this._url_cache = P.call(this, this._urs_options, t)
            }
            R.call(this)
        }
        if (t.needPrepare && !this.isInclude)
            x.call(this);
        this.box.style.display = "block";
        if (this._urs_options.afterShow)
            this._urs_options.afterShow.call(this)
    }
    ;
    window.URS.prototype.closeIframe = function() {
        var e = r[this.MGID];
        if (!this.isInclude) {
            this.box.style.display = "none";
            if (this.sto)
                this.sto = clearTimeout(this.sto);
            if (!e.needPrepare) {
                if (navigator.userAgent.indexOf("MSIE") > 0) {
                    var t = document.getElementById("x-URS-iframe" + this.MGID)
                      , i = t.contentWindow;
                    if (t) {
                        t.src = "about:blank";
                        try {
                            i.document.write("");
                            i.document.clear()
                        } catch (n) {}
                    }
                    var o = document.getElementById("x-panel" + this.MGID);
                    o.removeChild(t);
                    window.CollectGarbage()
                }
                this.box.innerHTML = ""
            }
        } else
            ;
    }
    ;
    window.URS.prototype.doMbUnLoginProxy = function() {
        var e = {
            proxyModule: "mbunlogin",
            doLoginProxy: 1
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.loginUnlock = function() {
        var e = {
            fromLoginLock: 1,
            lock: 0
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.loginDolock = function() {
        var e = {
            fromLoginLock: 1,
            lock: 1
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.regUnlock = function() {
        var e = {
            fromRegLock: 1,
            lock: 0
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.regDolock = function() {
        var e = {
            fromRegLock: 1,
            lock: 1
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.doLoginProxy = function(e) {
        var t = {
            username: e.username,
            pwd: e.pwd,
            defaultUnLogin: e.defaultUnLogin,
            doLoginProxy: 1
        };
        T.call(this, this.MGID, t)
    }
    ;
    window.URS.prototype.loginUnlockMb = function() {
        var e = {
            fromLoginLockMb: 1,
            lock: 0
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.loginDolockMb = function() {
        var e = {
            fromLoginLockMb: 1,
            lock: 1
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.regUnlockMb = function() {
        var e = {
            fromRegLockMb: 1,
            lock: 0
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.regDolockMb = function() {
        var e = {
            fromRegLockMb: 1,
            lock: 1
        };
        T.call(this, this.MGID, e)
    }
    ;
    window.URS.prototype.getIframeSize = function() {
        var e = {
            getIframeSize: 1
        };
        T.call(this, this.MGID, e);
    }
    ;
    window.URS.prototype.setMbloginClause = function(e) {
        var t = {
            fromMbSetClause: 1,
            mbloginClause: e
        };
        T.call(this, this.MGID, t)
    }
    ;
    window.URS.prototype.setMailloginClause = function(e) {
        var t = {
            fromMailSetClause: 1,
            mailloginClause: e
        };
        T.call(this, this.MGID, t)
    }
    ;
    window.URS.setPkidAndPd = function() {
        var e = {};
        var i = function(t) {
            var i, n;
            if (t && t.lgs) {
                i = t.lgs;
                n = t.pkid;
                window.URSCFG[n] = parseInt(i);
                e[n] && e[n](n)
            }
        };
        var n = function(e) {
            var n = e.pkid || "";
            var o = e.pd || "";
            var r;
            if (void 0 === e.mode)
                r = "3";
            else
                r = e.mode;
            if ("3" != r && "0" != r) {
                var s = "URSJSONP" + (new Date).getTime();
                window[s] = i;
                var a = "//dl.reg.163.com/dl/getConf?callback=" + s + "&pkid=" + n + "&pd=" + o + "&mode=" + r;
                var c = document.createElement("script");
                c.type = "text/javascript";
                c.id = "urs-script-" + s;
                if ("is_IPV6_Message" === t)
                    a = p(a);
                c.src = a;
                document.getElementsByTagName("head")[0].appendChild(c);
                setTimeout(function() {
                    document.getElementsByTagName("head")[0].removeChild(c)
                }, 5e3)
            }
        };
        return function(t) {
            t = t || {};
            var i = t.pkid || "";
            if ("function" == typeof t.pathbCallback)
                e[i] = t.pathbCallback;
            n(t)
        }
    }();
    return window.URS
});
(function() {
    function e(t, n) {
        function r(e) {
            if (r[e] !== v)
                return r[e];
            var t;
            if ("bug-string-char-index" == e)
                t = "a" != "a"[0];
            else if ("json" == e)
                t = r("json-stringify") && r("json-parse");
            else {
                var i;
                if ("json-stringify" == e) {
                    t = n.stringify;
                    var o = "function" == typeof t && w;
                    if (o) {
                        (i = function() {
                            return 1
                        }
                        ).toJSON = i;
                        try {
                            o = "0" === t(0) && "0" === t(new s) && '""' == t(new a) && t(p) === v && t(v) === v && t() === v && "1" === t(i) && "[1]" == t([i]) && "[null]" == t([v]) && "null" == t(null) && "[null,null,null]" == t([v, p, null]) && '{"a":[1,true,false,null,"\\u0000\\b\\n\\f\\r\\t"]}' == t({
                                a: [i, !0, !1, null, "\0\b\n\f\r\t"]
                            }) && "1" === t(null, i) && "[\n 1,\n 2\n]" == t([1, 2], null, 1) && '"-271821-04-20T00:00:00.000Z"' == t(new l((-864e13))) && '"+275760-09-13T00:00:00.000Z"' == t(new l(864e13)) && '"-000001-01-01T00:00:00.000Z"' == t(new l((-621987552e5))) && '"1969-12-31T23:59:59.999Z"' == t(new l((-1)))
                        } catch (c) {
                            o = !1
                        }
                    }
                    t = o
                }
                if ("json-parse" == e) {
                    t = n.parse;
                    if ("function" == typeof t)
                        try {
                            if (0 === t("0") && !t(!1)) {
                                i = t('{"a":[1,true,false,null,"\\u0000\\b\\n\\f\\r\\t"]}');
                                var f = 5 == i.a.length && 1 === i.a[0];
                                if (f) {
                                    try {
                                        f = !t('"\t"')
                                    } catch (u) {}
                                    if (f)
                                        try {
                                            f = 1 !== t("01")
                                        } catch (d) {}
                                    if (f)
                                        try {
                                            f = 1 !== t("1.")
                                        } catch (h) {}
                                }
                            }
                        } catch (g) {
                            f = !1
                        }
                    t = f
                }
            }
            return r[e] = !!t
        }
        t || (t = o.Object());
        n || (n = o.Object());
        var s = t.Number || o.Number
          , a = t.String || o.String
          , c = t.Object || o.Object
          , l = t.Date || o.Date
          , f = t.SyntaxError || o.SyntaxError
          , u = t.TypeError || o.TypeError
          , d = t.Math || o.Math
          , h = t.JSON || o.JSON;
        "object" == typeof h && h && (n.stringify = h.stringify,
        n.parse = h.parse);
        var c = c.prototype, p = c.toString, g, m, v, w = new l((-0xc782b5b800cec));
        try {
            w = -109252 == w.getUTCFullYear() && 0 === w.getUTCMonth() && 1 === w.getUTCDate() && 10 == w.getUTCHours() && 37 == w.getUTCMinutes() && 6 == w.getUTCSeconds() && 708 == w.getUTCMilliseconds()
        } catch (_) {}
        if (!r("json")) {
            var b = r("bug-string-char-index");
            if (!w)
                var y = d.floor
                  , S = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
                  , I = function(e, t) {
                    return S[t] + 365 * (e - 1970) + y((e - 1969 + (t = +(1 < t))) / 4) - y((e - 1901 + t) / 100) + y((e - 1601 + t) / 400)
                };
            (g = c.hasOwnProperty) || (g = function(e) {
                var t = {}, i;
                (t.__proto__ = null,
                t.__proto__ = {
                    toString: 1
                },
                t).toString != p ? g = function(e) {
                    var t = this.__proto__;
                    e = e in (this.__proto__ = null,
                    this);
                    this.__proto__ = t;
                    return e
                }
                : (i = t.constructor,
                g = function(e) {
                    var t = (this.constructor || i).prototype;
                    return e in this && !(e in t && this[e] === t[e])
                }
                );
                t = null;
                return g.call(this, e)
            }
            );
            m = function(e, t) {
                var n = 0, o, r, s;
                (o = function() {
                    this.valueOf = 0
                }
                ).prototype.valueOf = 0;
                r = new o;
                for (s in r)
                    g.call(r, s) && n++;
                o = r = null;
                n ? m = 2 == n ? function(e, t) {
                    var i = {}, n = "[object Function]" == p.call(e), o;
                    for (o in e)
                        n && "prototype" == o || g.call(i, o) || !(i[o] = 1) || !g.call(e, o) || t(o)
                }
                : function(e, t) {
                    var i = "[object Function]" == p.call(e), n, o;
                    for (n in e)
                        i && "prototype" == n || !g.call(e, n) || (o = "constructor" === n) || t(n);
                    (o || g.call(e, n = "constructor")) && t(n)
                }
                : (r = "valueOf toString toLocaleString propertyIsEnumerable isPrototypeOf hasOwnProperty constructor".split(" "),
                m = function(e, t) {
                    var n = "[object Function]" == p.call(e), o, s = !n && "function" != typeof e.constructor && i[typeof e.hasOwnProperty] && e.hasOwnProperty || g;
                    for (o in e)
                        n && "prototype" == o || !s.call(e, o) || t(o);
                    for (n = r.length; o = r[--n]; s.call(e, o) && t(o))
                        ;
                }
                );
                return m(e, t)
            }
            ;
            if (!r("json-stringify")) {
                var M = {
                    92: "\\\\",
                    34: '\\"',
                    8: "\\b",
                    12: "\\f",
                    10: "\\n",
                    13: "\\r",
                    9: "\\t"
                }
                  , k = function(e, t) {
                    return ("000000" + (t || 0)).slice(-e)
                }
                  , U = function(e) {
                    for (var t = '"', i = 0, n = e.length, o = !b || 10 < n, r = o && (b ? e.split("") : e); i < n; i++) {
                        var s = e.charCodeAt(i);
                        switch (s) {
                        case 8:
                        case 9:
                        case 10:
                        case 12:
                        case 13:
                        case 34:
                        case 92:
                            t += M[s];
                            break;
                        default:
                            if (32 > s) {
                                t += "\\u00" + k(2, s.toString(16));
                                break
                            }
                            t += o ? r[i] : e.charAt(i)
                        }
                    }
                    return t + '"'
                }
                  , C = function(e, t, i, n, o, r, s) {
                    var a, c, l, f, d, h, w, _, b;
                    try {
                        a = t[e]
                    } catch (S) {}
                    if ("object" == typeof a && a)
                        if (c = p.call(a),
                        "[object Date]" != c || g.call(a, "toJSON"))
                            "function" == typeof a.toJSON && ("[object Number]" != c && "[object String]" != c && "[object Array]" != c || g.call(a, "toJSON")) && (a = a.toJSON(e));
                        else if (a > -1 / 0 && a < 1 / 0) {
                            if (I) {
                                f = y(a / 864e5);
                                for (c = y(f / 365.2425) + 1970 - 1; I(c + 1, 0) <= f; c++)
                                    ;
                                for (l = y((f - I(c, 0)) / 30.42); I(c, l + 1) <= f; l++)
                                    ;
                                f = 1 + f - I(c, l);
                                d = (a % 864e5 + 864e5) % 864e5;
                                h = y(d / 36e5) % 24;
                                w = y(d / 6e4) % 60;
                                _ = y(d / 1e3) % 60;
                                d %= 1e3
                            } else
                                c = a.getUTCFullYear(),
                                l = a.getUTCMonth(),
                                f = a.getUTCDate(),
                                h = a.getUTCHours(),
                                w = a.getUTCMinutes(),
                                _ = a.getUTCSeconds(),
                                d = a.getUTCMilliseconds();
                            a = (0 >= c || 1e4 <= c ? (0 > c ? "-" : "+") + k(6, 0 > c ? -c : c) : k(4, c)) + "-" + k(2, l + 1) + "-" + k(2, f) + "T" + k(2, h) + ":" + k(2, w) + ":" + k(2, _) + "." + k(3, d) + "Z"
                        } else
                            a = null;
                    i && (a = i.call(t, e, a));
                    if (null === a)
                        return "null";
                    c = p.call(a);
                    if ("[object Boolean]" == c)
                        return "" + a;
                    if ("[object Number]" == c)
                        return a > -1 / 0 && a < 1 / 0 ? "" + a : "null";
                    if ("[object String]" == c)
                        return U("" + a);
                    if ("object" == typeof a) {
                        for (e = s.length; e--; )
                            if (s[e] === a)
                                throw u();
                        s.push(a);
                        b = [];
                        t = r;
                        r += o;
                        if ("[object Array]" == c) {
                            l = 0;
                            for (e = a.length; l < e; l++)
                                c = C(l, a, i, n, o, r, s),
                                b.push(c === v ? "null" : c);
                            e = b.length ? o ? "[\n" + r + b.join(",\n" + r) + "\n" + t + "]" : "[" + b.join(",") + "]" : "[]"
                        } else
                            m(n || a, function(e) {
                                var t = C(e, a, i, n, o, r, s);
                                t !== v && b.push(U(e) + ":" + (o ? " " : "") + t)
                            }),
                            e = b.length ? o ? "{\n" + r + b.join(",\n" + r) + "\n" + t + "}" : "{" + b.join(",") + "}" : "{}";
                        s.pop();
                        return e
                    }
                };
                n.stringify = function(e, t, n) {
                    var o, r, s, a;
                    if (i[typeof t] && t)
                        if ("[object Function]" == (a = p.call(t)))
                            r = t;
                        else if ("[object Array]" == a) {
                            s = {};
                            for (var c = 0, l = t.length, f; c < l; f = t[c++],
                            (a = p.call(f),
                            "[object String]" == a || "[object Number]" == a) && (s[f] = 1))
                                ;
                        }
                    if (n)
                        if ("[object Number]" == (a = p.call(n))) {
                            if (0 < (n -= n % 1))
                                for (o = "",
                                10 < n && (n = 10); o.length < n; o += " ")
                                    ;
                        } else
                            "[object String]" == a && (o = 10 >= n.length ? n : n.slice(0, 10));
                    return C("", (f = {},
                    f[""] = e,
                    f), r, s, o, "", [])
                }
            }
            if (!r("json-parse")) {
                var R = a.fromCharCode, D = {
                    92: "\\",
                    34: '"',
                    47: "/",
                    98: "\b",
                    116: "\t",
                    110: "\n",
                    102: "\f",
                    114: "\r"
                }, T, x, O = function() {
                    T = x = null;
                    throw f()
                }, j = function() {
                    for (var e = x, t = e.length, i, n, o, r, s; T < t; )
                        switch (s = e.charCodeAt(T),
                        s) {
                        case 9:
                        case 10:
                        case 13:
                        case 32:
                            T++;
                            break;
                        case 123:
                        case 125:
                        case 91:
                        case 93:
                        case 58:
                        case 44:
                            return i = b ? e.charAt(T) : e[T],
                            T++,
                            i;
                        case 34:
                            i = "@";
                            for (T++; T < t; )
                                if (s = e.charCodeAt(T),
                                32 > s)
                                    O();
                                else if (92 == s)
                                    switch (s = e.charCodeAt(++T),
                                    s) {
                                    case 92:
                                    case 34:
                                    case 47:
                                    case 98:
                                    case 116:
                                    case 110:
                                    case 102:
                                    case 114:
                                        i += D[s];
                                        T++;
                                        break;
                                    case 117:
                                        n = ++T;
                                        for (o = T + 4; T < o; T++)
                                            s = e.charCodeAt(T),
                                            48 <= s && 57 >= s || 97 <= s && 102 >= s || 65 <= s && 70 >= s || O();
                                        i += R("0x" + e.slice(n, T));
                                        break;
                                    default:
                                        O()
                                    }
                                else {
                                    if (34 == s)
                                        break;
                                    s = e.charCodeAt(T);
                                    for (n = T; 32 <= s && 92 != s && 34 != s; )
                                        s = e.charCodeAt(++T);
                                    i += e.slice(n, T)
                                }
                            if (34 == e.charCodeAt(T))
                                return T++,
                                i;
                            O();
                        default:
                            n = T;
                            45 == s && (r = !0,
                            s = e.charCodeAt(++T));
                            if (48 <= s && 57 >= s) {
                                for (48 == s && (s = e.charCodeAt(T + 1),
                                48 <= s && 57 >= s) && O(); T < t && (s = e.charCodeAt(T),
                                48 <= s && 57 >= s); T++)
                                    ;
                                if (46 == e.charCodeAt(T)) {
                                    for (o = ++T; o < t && (s = e.charCodeAt(o),
                                    48 <= s && 57 >= s); o++)
                                        ;
                                    o == T && O();
                                    T = o
                                }
                                s = e.charCodeAt(T);
                                if (101 == s || 69 == s) {
                                    s = e.charCodeAt(++T);
                                    43 != s && 45 != s || T++;
                                    for (o = T; o < t && (s = e.charCodeAt(o),
                                    48 <= s && 57 >= s); o++)
                                        ;
                                    o == T && O();
                                    T = o
                                }
                                return +e.slice(n, T)
                            }
                            r && O();
                            if ("true" == e.slice(T, T + 4))
                                return T += 4,
                                !0;
                            if ("false" == e.slice(T, T + 5))
                                return T += 5,
                                !1;
                            if ("null" == e.slice(T, T + 4))
                                return T += 4,
                                null;
                            O()
                        }
                    return "$"
                }, E = function(e) {
                    var t, i;
                    "$" == e && O();
                    if ("string" == typeof e) {
                        if ("@" == (b ? e.charAt(0) : e[0]))
                            return e.slice(1);
                        if ("[" == e) {
                            for (t = []; ; i || (i = !0)) {
                                e = j();
                                if ("]" == e)
                                    break;
                                i && ("," == e ? (e = j(),
                                "]" == e && O()) : O());
                                "," == e && O();
                                t.push(E(e))
                            }
                            return t
                        }
                        if ("{" == e) {
                            for (t = {}; ; i || (i = !0)) {
                                e = j();
                                if ("}" == e)
                                    break;
                                i && ("," == e ? (e = j(),
                                "}" == e && O()) : O());
                                "," != e && "string" == typeof e && "@" == (b ? e.charAt(0) : e[0]) && ":" == j() || O();
                                t[e.slice(1)] = E(j())
                            }
                            return t
                        }
                        O()
                    }
                    return e
                }, G = function(e, t, i) {
                    i = B(e, t, i);
                    i === v ? delete e[t] : e[t] = i
                }, B = function(e, t, i) {
                    var n = e[t], o;
                    if ("object" == typeof n && n)
                        if ("[object Array]" == p.call(n))
                            for (o = n.length; o--; )
                                G(n, o, i);
                        else
                            m(n, function(e) {
                                G(n, e, i)
                            });
                    return i.call(e, t, n)
                };
                n.parse = function(e, t) {
                    var i, n;
                    T = 0;
                    x = "" + e;
                    i = E(j());
                    "$" != j() && O();
                    T = x = null;
                    return t && "[object Function]" == p.call(t) ? B((n = {},
                    n[""] = i,
                    n), "", t) : i
                }
            }
        }
        n.runInContext = e;
        return n
    }
    var t = "function" == typeof define && define.amd
      , i = {
        "function": !0,
        object: !0
    }
      , n = i[typeof exports] && exports && !exports.nodeType && exports
      , o = i[typeof window] && window || this
      , r = n && i[typeof module] && module && !module.nodeType && "object" == typeof global && global;
    !r || r.global !== r && r.window !== r && r.self !== r || (o = r);
    if (n && !t)
        e(o, n);
    else {
        var s = o.JSON
          , a = o.JSON3
          , c = !1
          , l = e(o, o.JSON3 = {
            noConflict: function() {
                c || (c = !0,
                o.JSON = s,
                o.JSON3 = a,
                s = a = null);
                return l
            }
        });
        o.JSON = {
            parse: l.parse,
            stringify: l.stringify
        }
    }
    t && define("URS-JSON3", function() {
        return l
    })
}
).call(this);
