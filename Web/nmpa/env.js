window = new Object();
function randomString(len) {
  len = len || 32;
  var $chars = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678";
  /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
  var maxPos = $chars.length;
  var pwd = "";
  for (i = 0; i < len; i++) {
    pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
  }
  return pwd;
}
var myElements = {
  meta: [
    { charset: "utf-8" },
    { "http-equiv": "X-UA-Compatible", content: "IE=edge,chrome=1" },
    { name: "SiteIDCode", content: "bm35000001" },
    { name: "SiteName", content: "国家药品监督管理局" },
    { name: "SiteDomain", content: "www.nmpa.gov.cn" },
    {
      content:
        "{q!x7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,txt,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipaqqqqqqqqqqqqqqqHUJxXgCu2M5w.gCVqqqQcp95tsazingZhsLXHn35tOg3HSWd~RKtGMnGBmoW3AbCiFFHL44p_Mkg7eaCvPDdZ.fKikc5QuGp5tELEX0rvpt7ZifDHwF8a6bpHSiI91bCjio40V7DiCWt3aGa52hdqFfccFH3WB2KiklMqdzG4vqXZLGCX9ExlR.biVtyQegSF0lyl_Psj5cNVqCO84F4LT0OCPiLVaNOX4FweOfkCLqRGcjktr3tGTnatoij74aGjrmNgr9KiaqWZnvkBEthrj.sMDWWaqvsJstVWCWpzowCYBWb9SMse63PLnM03XMGrNqlAIAuxEw6mBxb92M1z6IPLXJKWCUnL7kTW8InfB32GEhSNgWPf.8AeVif988SpfkmEZArRkq03{XrOZ0rsJaHcevJDZ9RurNJnGS3nYzEUER3ufTEvVg3nJnoUEGwkmfJDRGHDQ5M292MOwLEC9TRbGZFkJfFkTaJDldQOr0svW13SrtqbGkQapfqaGhttps:3Dw11rlzTZkWI3TUmRrjQA:443k642l5120hQiR2.AHPrxLhUKFztca4ZOEr1.LL2WZ_MdGPF0SfipT9A07JOvqXep2bXulezaMAoU8r7r4r0}!JO0tYmfiA07KJlZSV6ZVtTZGVPr3Rr3XVvVVmb92KcwRhYE1FKaKEYQeVCaVc9wOVCwUEKEMrSffDKaVsf2NWmltps73W0SXRkfpqC30FYQDVY7kASlDWqyFVcN6ovL98qLcxlywQArDHCQYQAxcl9rFUawyW2Vyqkzoo2YcVfr0pomImGfUl0H2c_JuZYuPr8y00A468XYM4UCSVBxyuY4zmhWqqqqqqqqqqqqqqqlhTGqkID3qlm5lg*QI992W2S_1Og4hnwdhqaEEsGZDsGIJARvmGQdw0AJlcE1JmE6cu31r2x51p3ihaLhku2xJqAKiP7Qt0QsWAEYx2S1xAQhrfxolr91q1JcUmQ7cpL9J9QUD0GdxOELkSLwmuW0Es23pcqAcpEpVfqhlShwVjJog1ostX3jus6TlHTh5VMbmBGEgruzUhQ2gqBOl.aAyrh5E4eQTS.VsZQSZsuHi59FTTkccWgFyA.xo4Tl5SkVl7y1uABElBf1fkHHhRGgacM8iH9Mdmk_DBgMSfOBl7rQPcUwceG1bpkklz7O2muNpZ9VO9OWlIqe6ucpWFAMZsX.Dj0Iy918lhW1jTtbc_V12ThNhhLZOOMCsjJi_qngoy7jvS5ShNqK2TuzxM3hzphCltg17cHSUELb7nvKxx9IPpkJlR0K095jEFEn7rdhphl27mnnVRLQvG4qDRVA2qnslLqM2AnKmzp1GanJD_AOTfcilNqO0YnLhxQFKr2vDDZHMPr.ll2DISmkWT0gt0YplUgs3mJOcbEsV2WnoPrhIpNmh6GTpq9O10Z5VpYBmT0s820bxoWtQfWulYVss1EiUVl_Qprom2WRVq9FmUax1cybtVZH8agWpUApppJwVTatUSJNVSQFrOpoDAqpqpSYcq0QRkgWoo0oUklrUU79hqLBlCGpWrWjEbzwE1NZcnqCDl2ZWPqvoONghOa7cl0wkvmmkSlGluNsiAL0laps8rYOru9tWGL4iDyWYc9Htq9ZinGaV1pwUcAxcGAspplIlaQPAm0oWqamc1V5m0AMln081f9iEq9cVV3gK9VPlAZsmTW1cflsETJwmi9VSSBnHi3L_svsW8Ln4lBypeZF5TCSxiEtgpiPlILsdcteUIgG_ssTsdgQysMIrwlejkI.tF7g_a_dpQVp_fHWVZZtufH5Vg319ksLJ8ZAgrUpWXljCcMqid07nG.8U3L96a.8lyZpapHRENNwu1Fr1X3Anu.pszNoZGBSoI2p9aKOHXrmbrDSl_2sjqj.lyVcypDdl_QPSGqr2Da67074t1083179040hgu_b7Ub26.xYQ0IlkFQr2xJSPUJmNI6Hxr0V35R10mssYzfp6YBRVzT1qr0r7",
      parentNode: {
        removeChild: function (name) {},
      },
    },
  ],
  myPlugin: [
    {
      0: "",
      "application/x-google-chrome-pdf": "",
      name: "Chrome PDF Plugin",
      filename: "internal-pdf-viewer",
      description: "Portable Document Format",
      length: 1,
    },
    {
      0: "",
      "application/pdf": "",
      name: "Chrome PDF Viewer",
      filename: "mhjfbmdgcfjbbpaeojofohoefgiehjai",
      description: "",
      length: 1,
    },
  ],
  script: [
    {
      type: "text/javascript",
      charset: "iso-8859-1",
      src: "/ZvbYc1RuNkYg/h2XbjSpBo3BD.a670748.js",
      r: "m",
      getAttribute: function getAttribute(name) {
        return "m";
      },
      parentElement: {
        removeChild: function removeChild(name) {},
      },
      parentNode: {
        removeChild: function (name) {},
      },
    },
  ],
  localStorage: {},
};
!(() => {
  "use strict";
  const $toString = Function.toString;
  const myFunction_toString_symbol = Symbol(
    "(".concat("", ")_", (Math.random() + "").toString(36))
  );
  const myToString = function () {
    return (
      (typeof this == "function" && this[myFunction_toString_symbol]) ||
      $toString.call(this)
    );
  };
  function set_native(func, key, value) {
    Object.defineProperty(func, key, {
      enumerable: false,
      configurable: true,
      writable: true,
      value: value,
    });
  }
  delete Function.prototype["toString"];
  set_native(Function.prototype, "toString", myToString);
  set_native(
    Function.prototype.toString,
    myFunction_toString_symbol,
    "function toString() { [native code] }"
  );
  window.safeFunction = (func) => {
    set_native(
      func,
      myFunction_toString_symbol,
      `function ${
        (myFunction_toString_symbol, func.name || "")
      }(){ [native code] }`
    );
  };
}).call(window);

var Location = function Location() {};
window.safeFunction(Location);
Object.defineProperties(Location.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "Location",
    configurable: true,
  },
});
/**
 * envLocation
 */
Location.prototype.hash = "";
Location.prototype.host = "www.nmpa.gov.cn";
Location.prototype.hostname = "www.nmpa.gov.cn";
Location.prototype.href = "https://www.nmpa.gov.cn/";
Location.prototype.origin = "https://www.nmpa.gov.cn";
Location.prototype.pathname = "/";
Location.prototype.port = "";
Location.prototype.protocol = "https:";
Location.prototype.search = "";
Location.prototype.replace = function replace(p) {
  console.log("Location.prototype.replace", p);
};

var location = {};
location.__proto__ = Location;
location.prototype = Location.prototype;

/**
 * envDocument
 */
var EventTarget = function EventTarget() {};
window.safeFunction(EventTarget);
Object.defineProperties(EventTarget.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "EventTarget",
    configurable: true,
  },
});
EventTarget.prototype.addEventListener = function addEventListener(
  type,
  listener,
  _
) {
  /**
   * type 表示监听事件类型的大小写敏感的字符串
   * listener 当所监听的事件类型触发时，会接收到一个事件通知（实现了 Event 接口的对象）对象。listener 必须是一个实现了 EventListener 接口的对象，或者是一个函数。
   */
};
window.safeFunction(EventTarget.prototype.addEventListener);
EventTarget.prototype.dispatchEvent = function dispatchEvent() {};
window.safeFunction(EventTarget.prototype.dispatchEvent);
EventTarget.prototype.removeEventListener = function removeEventListener() {};
window.safeFunction(EventTarget.prototype.removeEventListener);
var Node = function Node() {};
window.safeFunction(Node);
Object.defineProperties(Node.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "Node",
    configurable: true,
  },
});
Node.__proto__ = EventTarget;
Node.prototype = EventTarget.prototype;
Node.prototype.ATTRIBUTE_NODE = 2;
Node.prototype.CDATA_SECTION_NODE = 4;
Node.prototype.COMMENT_NODE = 8;
Node.prototype.DOCUMENT_FRAGMENT_NODE = 11;
Node.prototype.DOCUMENT_NODE = 9;
Node.prototype.DOCUMENT_POSITION_CONTAINED_BY = 16;
Node.prototype.DOCUMENT_POSITION_CONTAINS = 8;
Node.prototype.DOCUMENT_POSITION_DISCONNECTED = 1;
Node.prototype.DOCUMENT_POSITION_FOLLOWING = 4;
Node.prototype.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 32;
Node.prototype.DOCUMENT_POSITION_PRECEDING = 2;
Node.prototype.DOCUMENT_TYPE_NODE = 10;
Node.prototype.ELEMENT_NODE = 1;
Node.prototype.ENTITY_NODE = 6;
Node.prototype.ENTITY_REFERENCE_NODE = 5;
Node.prototype.NOTATION_NODE = 12;
Node.prototype.PROCESSING_INSTRUCTION_NODE = 7;
Node.prototype.TEXT_NODE = 3;
Node.prototype.appendChild = function appendChild() {};
window.safeFunction(Node.prototype.appendChild);
Node.prototype.cloneNode = function cloneNode() {};
window.safeFunction(Node.prototype.cloneNode);
Node.prototype.compareDocumentPosition = function compareDocumentPosition() {};
window.safeFunction(Node.prototype.compareDocumentPosition);
Node.prototype.contains = function contains() {};
window.safeFunction(Node.prototype.contains);
Node.prototype.getRootNode = function getRootNode() {};
window.safeFunction(Node.prototype.getRootNode);
Node.prototype.hasChildNodes = function hasChildNodes() {};
window.safeFunction(Node.prototype.hasChildNodes);
Node.prototype.insertBefore = function insertBefore() {};
window.safeFunction(Node.prototype.insertBefore);
Node.prototype.isDefaultNamespace = function isDefaultNamespace() {};
window.safeFunction(Node.prototype.isDefaultNamespace);
Node.prototype.isEqualNode = function isEqualNode() {};
window.safeFunction(Node.prototype.isEqualNode);
Node.prototype.isSameNode = function isSameNode() {};
window.safeFunction(Node.prototype.isSameNode);
Node.prototype.lookupNamespaceURI = function lookupNamespaceURI() {};
window.safeFunction(Node.prototype.lookupNamespaceURI);
Node.prototype.lookupPrefix = function lookupPrefix() {};
window.safeFunction(Node.prototype.lookupPrefix);
Node.prototype.normalize = function normalize() {};
window.safeFunction(Node.prototype.normalize);
Node.prototype.removeChild = function removeChild() {};
window.safeFunction(Node.prototype.removeChild);
Node.prototype.replaceChild = function replaceChild() {};
window.safeFunction(Node.prototype.replaceChild);
var Element = function Element() {};
window.safeFunction(Element);
Element.__proto__ = Node;
Element.prototype = Node.prototype;
Element.prototype.after = function after() {};
window.safeFunction(Element.prototype.after);
Element.prototype.animate = function animate() {};
window.safeFunction(Element.prototype.animate);
Element.prototype.append = function append() {};
window.safeFunction(Element.prototype.append);
Element.prototype.attachShadow = function attachShadow() {};
window.safeFunction(Element.prototype.attachShadow);
Element.prototype.before = function before() {};
window.safeFunction(Element.prototype.before);
Element.prototype.checkVisibility = function checkVisibility() {};
window.safeFunction(Element.prototype.checkVisibility);
Element.prototype.closest = function closest() {};
window.safeFunction(Element.prototype.closest);
Element.prototype.computedStyleMap = function computedStyleMap() {};
window.safeFunction(Element.prototype.computedStyleMap);
Element.prototype.getAnimations = function getAnimations() {};
window.safeFunction(Element.prototype.getAnimations);
Element.prototype.getAttribute = function getAttribute() {};
window.safeFunction(Element.prototype.getAttribute);
Element.prototype.getAttributeNS = function getAttributeNS() {};
window.safeFunction(Element.prototype.getAttributeNS);
Element.prototype.getAttributeNames = function getAttributeNames() {};
window.safeFunction(Element.prototype.getAttributeNames);
Element.prototype.getAttributeNode = function getAttributeNode() {};
window.safeFunction(Element.prototype.getAttributeNode);
Element.prototype.getAttributeNodeNS = function getAttributeNodeNS() {};
window.safeFunction(Element.prototype.getAttributeNodeNS);
Element.prototype.getBoundingClientRect = function getBoundingClientRect() {};
window.safeFunction(Element.prototype.getBoundingClientRect);
Element.prototype.getClientRects = function getClientRects() {};
window.safeFunction(Element.prototype.getClientRects);
Element.prototype.getElementsByClassName = function getElementsByClassName() {};
window.safeFunction(Element.prototype.getElementsByClassName);
Element.prototype.getElementsByTagName = function getElementsByTagName(
  tagName
) {
  let total = myElements[tagName];
  if (total === undefined) {
    return (myElements[tagName] = []), myElements[tagName];
  } else {
    return total;
  }
};
window.safeFunction(Element.prototype.getElementsByTagName);
Element.prototype.getElementsByTagNameNS = function getElementsByTagNameNS() {};
window.safeFunction(Element.prototype.getElementsByTagNameNS);
Element.prototype.getInnerHTML = function getInnerHTML() {};
window.safeFunction(Element.prototype.getInnerHTML);
Element.prototype.hasAttribute = function hasAttribute() {};
window.safeFunction(Element.prototype.hasAttribute);
Element.prototype.hasAttributeNS = function hasAttributeNS() {};
window.safeFunction(Element.prototype.hasAttributeNS);
Element.prototype.hasAttributes = function hasAttributes() {};
window.safeFunction(Element.prototype.hasAttributes);
Element.prototype.hasPointerCapture = function hasPointerCapture() {};
window.safeFunction(Element.prototype.hasPointerCapture);
Element.prototype.insertAdjacentElement = function insertAdjacentElement() {};
window.safeFunction(Element.prototype.insertAdjacentElement);
Element.prototype.insertAdjacentHTML = function insertAdjacentHTML() {};
window.safeFunction(Element.prototype.insertAdjacentHTML);
Element.prototype.insertAdjacentText = function insertAdjacentText() {};
window.safeFunction(Element.prototype.insertAdjacentText);
Element.prototype.matches = function matches() {};
window.safeFunction(Element.prototype.matches);
Element.prototype.prepend = function prepend() {};
window.safeFunction(Element.prototype.prepend);
Element.prototype.querySelector = function querySelector() {};
window.safeFunction(Element.prototype.querySelector);
Element.prototype.querySelectorAll = function querySelectorAll() {};
window.safeFunction(Element.prototype.querySelectorAll);
Element.prototype.releasePointerCapture = function releasePointerCapture() {};
window.safeFunction(Element.prototype.releasePointerCapture);
Element.prototype.remove = function remove() {};
window.safeFunction(Element.prototype.remove);
Element.prototype.removeAttribute = function removeAttribute() {};
window.safeFunction(Element.prototype.removeAttribute);
Element.prototype.removeAttributeNS = function removeAttributeNS() {};
window.safeFunction(Element.prototype.removeAttributeNS);
Element.prototype.removeAttributeNode = function removeAttributeNode() {};
window.safeFunction(Element.prototype.removeAttributeNode);
Element.prototype.replaceChildren = function replaceChildren() {};
window.safeFunction(Element.prototype.replaceChildren);
Element.prototype.replaceWith = function replaceWith() {};
window.safeFunction(Element.prototype.replaceWith);
Element.prototype.requestFullscreen = function requestFullscreen() {};
window.safeFunction(Element.prototype.requestFullscreen);
Element.prototype.requestPointerLock = function requestPointerLock() {};
window.safeFunction(Element.prototype.requestPointerLock);
Element.prototype.scroll = function scroll() {};
window.safeFunction(Element.prototype.scroll);
Element.prototype.scrollBy = function scrollBy() {};
window.safeFunction(Element.prototype.scrollBy);
Element.prototype.scrollIntoView = function scrollIntoView() {};
window.safeFunction(Element.prototype.scrollIntoView);
Element.prototype.scrollIntoViewIfNeeded = function scrollIntoViewIfNeeded() {};
window.safeFunction(Element.prototype.scrollIntoViewIfNeeded);
Element.prototype.scrollTo = function scrollTo() {};
window.safeFunction(Element.prototype.scrollTo);
Element.prototype.setAttribute = function setAttribute() {};
window.safeFunction(Element.prototype.setAttribute);
Element.prototype.setAttributeNS = function setAttributeNS() {};
window.safeFunction(Element.prototype.setAttributeNS);
Element.prototype.setAttributeNode = function setAttributeNode() {};
window.safeFunction(Element.prototype.setAttributeNode);
Element.prototype.setAttributeNodeNS = function setAttributeNodeNS() {};
window.safeFunction(Element.prototype.setAttributeNodeNS);
Element.prototype.setHTML = function setHTML() {};
window.safeFunction(Element.prototype.setHTML);
Element.prototype.setPointerCapture = function setPointerCapture() {};
window.safeFunction(Element.prototype.setPointerCapture);
Element.prototype.toggleAttribute = function toggleAttribute() {};
window.safeFunction(Element.prototype.toggleAttribute);
Element.prototype.webkitMatchesSelector = function webkitMatchesSelector() {};
window.safeFunction(Element.prototype.webkitMatchesSelector);
Element.prototype.webkitRequestFullScreen =
  function webkitRequestFullScreen() {};
window.safeFunction(Element.prototype.webkitRequestFullScreen);
Element.prototype.webkitRequestFullscreen =
  function webkitRequestFullscreen() {};
window.safeFunction(Element.prototype.webkitRequestFullscreen);
var Document = function Document() {};
window.safeFunction(Document);
Object.defineProperties(Document.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "Document",
    configurable: true,
  },
});
Document.__proto__ = Node;
Document.prototype = Node.prototype;
Document.prototype.adoptNode = function adoptNode() {};
window.safeFunction(Document.prototype.adoptNode);
Document.prototype.append = function append() {};
window.safeFunction(Document.prototype.append);
Document.prototype.captureEvents = function captureEvents() {};
window.safeFunction(Document.prototype.captureEvents);
Document.prototype.caretRangeFromPoint = function caretRangeFromPoint() {};
window.safeFunction(Document.prototype.caretRangeFromPoint);
Document.prototype.clear = function clear() {};
window.safeFunction(Document.prototype.clear);
Document.prototype.close = function close() {};
window.safeFunction(Document.prototype.close);
Document.prototype.createAttribute = function createAttribute() {};
window.safeFunction(Document.prototype.createAttribute);
Document.prototype.createAttributeNS = function createAttributeNS() {};
window.safeFunction(Document.prototype.createAttributeNS);
Document.prototype.createCDATASection = function createCDATASection() {};
window.safeFunction(Document.prototype.createCDATASection);
Document.prototype.createComment = function createComment() {};
window.safeFunction(Document.prototype.createComment);
Document.prototype.createDocumentFragment =
  function createDocumentFragment() {};
window.safeFunction(Document.prototype.createDocumentFragment);
Document.prototype.createElement = function createElement(tagName, _) {
  if (tagName === "canvas") {
    return new CanvasElement();
  } else {
    var env_element_ = new Element();
    return env_element_;
  }
};
window.safeFunction(Document.prototype.createElement);
Document.prototype.createElementNS = function createElementNS() {};
window.safeFunction(Document.prototype.createElementNS);
Document.prototype.createEvent = function createEvent() {};
window.safeFunction(Document.prototype.createEvent);
Document.prototype.createExpression = function createExpression() {};
window.safeFunction(Document.prototype.createExpression);
Document.prototype.createNSResolver = function createNSResolver() {};
window.safeFunction(Document.prototype.createNSResolver);
Document.prototype.createNodeIterator = function createNodeIterator() {};
window.safeFunction(Document.prototype.createNodeIterator);
Document.prototype.createProcessingInstruction =
  function createProcessingInstruction() {};
window.safeFunction(Document.prototype.createProcessingInstruction);
Document.prototype.createRange = function createRange() {};
window.safeFunction(Document.prototype.createRange);
Document.prototype.createTextNode = function createTextNode() {};
window.safeFunction(Document.prototype.createTextNode);
Document.prototype.createTreeWalker = function createTreeWalker() {};
window.safeFunction(Document.prototype.createTreeWalker);
Document.prototype.elementFromPoint = function elementFromPoint() {};
window.safeFunction(Document.prototype.elementFromPoint);
Document.prototype.elementsFromPoint = function elementsFromPoint() {};
window.safeFunction(Document.prototype.elementsFromPoint);
Document.prototype.evaluate = function evaluate() {};
window.safeFunction(Document.prototype.evaluate);
Document.prototype.execCommand = function execCommand() {};
window.safeFunction(Document.prototype.execCommand);
Document.prototype.exitFullscreen = function exitFullscreen() {};
window.safeFunction(Document.prototype.exitFullscreen);
Document.prototype.exitPictureInPicture = function exitPictureInPicture() {};
window.safeFunction(Document.prototype.exitPictureInPicture);
Document.prototype.exitPointerLock = function exitPointerLock() {};
window.safeFunction(Document.prototype.exitPointerLock);
Document.prototype.getAnimations = function getAnimations() {};
window.safeFunction(Document.prototype.getAnimations);
Document.prototype.getElementById = function getElementById(tagName) {
  if (tagName == "__anchor__") {
    return null;
  } else if (tagName == "__onload__") {
    return {
      id: "__onload__",
      name: "iM4tqucEJqB7eqF.EKjQHX47mTG6wdHKBTR7NVmh3nI4UhkCMxQlA2ehO0KSxygXNqoPKSgktP9NeObCcdclia",
      defaultValue: "DunyPZ2nBsoMRWk_BPT9ZA",
      value: "DunyPZ2nBsoMRWk_BPT9ZA",
      nodeName: "INPUT",
      nodeType: 1,
      type: "hidden",
      nextSibling: {
        assignedSlot: null,
        baseURI: "https://www.nmpa.gov.cn/",
        childNodes: [],
        data: "\n\n\n\n",
        firstChild: null,
        isConnected: true,
        lastChild: null,
        length: 4,
        nextElementSibling: null,
        nextSibling: null,
        nodeName: "#text",
        nodeType: 3,
        nodeValue: "\n\n\n\n",
        textContent: "\n\n\n\n",
        wholeText: "\n\n\n\n",
      },
      getAttribute: function getAttribute(tagName) {
        if (tagName == "onclick") {
          return null;
        } else if (tagName == "onsubmit") {
          return null;
        }
      },
      firstChild: null,
    };
  }
};
window.safeFunction(Document.prototype.getElementById);
Document.prototype.getElementsByClassName =
  function getElementsByClassName() {};
window.safeFunction(Document.prototype.getElementsByClassName);
Document.prototype.getElementsByName = function getElementsByName() {};
window.safeFunction(Document.prototype.getElementsByName);
Document.prototype.getElementsByTagName = function getElementsByTagName(
  tagName
) {
  let total = myElements[tagName];
  if (total === undefined) {
    return (myElements[tagName] = []), myElements[tagName];
  } else {
    return total;
  }
};
window.safeFunction(Document.prototype.getElementsByTagName);
Document.prototype.getElementsByTagNameNS =
  function getElementsByTagNameNS() {};
window.safeFunction(Document.prototype.getElementsByTagNameNS);
Document.prototype.getSelection = function getSelection() {};
window.safeFunction(Document.prototype.getSelection);
Document.prototype.hasFocus = function hasFocus() {};
window.safeFunction(Document.prototype.hasFocus);
Document.prototype.importNode = function importNode() {};
window.safeFunction(Document.prototype.importNode);
Document.prototype.open = function open() {};
window.safeFunction(Document.prototype.open);
Document.prototype.prepend = function prepend() {};
window.safeFunction(Document.prototype.prepend);
Document.prototype.queryCommandEnabled = function queryCommandEnabled() {};
window.safeFunction(Document.prototype.queryCommandEnabled);
Document.prototype.queryCommandIndeterm = function queryCommandIndeterm() {};
window.safeFunction(Document.prototype.queryCommandIndeterm);
Document.prototype.queryCommandState = function queryCommandState() {};
window.safeFunction(Document.prototype.queryCommandState);
Document.prototype.queryCommandSupported = function queryCommandSupported() {};
window.safeFunction(Document.prototype.queryCommandSupported);
Document.prototype.queryCommandValue = function queryCommandValue() {};
window.safeFunction(Document.prototype.queryCommandValue);
Document.prototype.querySelector = function querySelector() {};
window.safeFunction(Document.prototype.querySelector);
Document.prototype.querySelectorAll = function querySelectorAll() {};
window.safeFunction(Document.prototype.querySelectorAll);
Document.prototype.releaseEvents = function releaseEvents() {};
window.safeFunction(Document.prototype.releaseEvents);
Document.prototype.replaceChildren = function replaceChildren() {};
window.safeFunction(Document.prototype.replaceChildren);
Document.prototype.webkitCancelFullScreen =
  function webkitCancelFullScreen() {};
window.safeFunction(Document.prototype.webkitCancelFullScreen);
Document.prototype.webkitExitFullscreen = function webkitExitFullscreen() {};
window.safeFunction(Document.prototype.webkitExitFullscreen);
Document.prototype.write = function write() {};
window.safeFunction(Document.prototype.write);
Document.prototype.writeln = function writeln() {};
window.safeFunction(Document.prototype.writeln);
var HTMLDocument = function HTMLDocument() {};
window.safeFunction(HTMLDocument);
Object.defineProperties(HTMLDocument.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "HTMLDocument",
    configurable: true,
  },
});
HTMLDocument.__proto__ = Document;
HTMLDocument.prototype = Document.prototype;
var document = new HTMLDocument();
function randomString__(length) {
  var result = "";
  var chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (var i = length; i > 0; --i) {
    result += chars[Math.floor(Math.random() * chars.length)];
  }
  return result;
}
var canvasBaseData =
  randomString__(36) +
  "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";

function CanvasElement() {
  this.attr = {};
  this.nodeName = "CANVAS";
  this.baseURI = "https://xiaomi.com";
  this.localName = "canvas";
  this.contentEditable = "inherit";
  this.setAttribute = function (name, value) {
    this.attr[name] = value;
  };
  this.getContext = function () {
    return {
      canvas: this,
      save: function () {},

      rect: function (a, b, c, d) {},

      isPointInPath: function (a, b, c) {
        return false;
      },

      createLinearGradient: function (a, b, c, d) {
        return {
          addColorStop: function (a, b) {},
        };
      },
      restore: function () {},
      translate: function (a, b) {},
      beginPath: function (a, b) {},
      closePath: function () {},
      arc: function (a, b, c, d, e) {},
      fill: function () {},
      fillText: function () {},
      stroke: function () {},
      fillRect: function () {},
      fillStyle: "#000000",
    };
  };
  this.toDataURL = function (type, quality) {
    try {
      if (typeof quality === "undefined") {
        quality = 0.92;
      }
      var attrs = JSON.stringify(this.attr);
      // 同一type不同quality返回url不同
      var finalData = codeHandler.encode(
        Math.floor(quality * 100) + attrs + canvasBaseData,
        "base64"
      );
      if (type === "image/jpeg") {
        return "data:image/jpeg;base64," + finalData;
      } else {
        return "data:image/png;base64," + finalData;
      }
    } catch (e) {
      log(e.stack);
      return "asdfafd";
    }
  };
}
document.URL = "https://www.nmpa.gov.cn/";
document.activeElement = "";
document.anchors = [];
document.characterSet = "UTF-8";
document.charset = "UTF-8";
document.childElementCount = 1;
document.children = ["html"];
document.compatMode = "BackCompat";
document.contentType = "text/html";
document.cookie = "";
document.currentScript = null;
document.defaultView = window;
document.designMode = "off";
document.dir = "";
document.doctype = null;
// document.documentElement = "";
document.documentURI = "https://www.nmpa.gov.cn/";
document.domain = "www.nmpa.gov.cn";
// document.embeds = "";
// document.featurePolicy = "";
document.fgColor = "";
// document.firstElementChild = "";
// document.fonts = "";
// document.forms = "";
// document.fragmentDirective = "";
document.fullscreen = false;
document.fullscreenElement = null;
document.fullscreenEnabled = true;
// document.head = "";
document.hidden = true;
// document.images = "";
// document.implementation = "";
document.inputEncoding = "UTF-8";
// document.links = "";
document.body = {
  nodeType: 1,
  nodeName: "BODY",
  tagName: "BODY",
  firstChild: {
    nodeType: 3,
    nodeName: "#text",
    nextSibling: {
      id: "__onload__",
      name: "iM4tqucEJqB7eqF.EKjQHX47mTG6wdHKBTR7NVmh3nI4UhkCMxQlA2ehO0KSxygXNqoPKSgktP9NeObCcdclia",
      defaultValue: "DunyPZ2nBsoMRWk_BPT9ZA",
      nodeName: "INPUT",
      nodeType: 1,
      type: "hidden",
      nextSibling: null,
      getAttribute: function getAttribute(tagName) {
        if (tagName == "onclick") {
          return null;
        } else if (tagName == "onsubmit") {
          return null;
        }
      },
      firstChild: null,
    },
    firstChild: null,
  },
  nextSibling: null,
  getAttribute: function getAttribute(tagName) {
    if (tagName == "onload") {
      return null;
    } else if (tagName == "onclick") {
      return null;
    } else if (tagName == "onsubmit") {
      return null;
    } else {
      return this[tagName];
    }
  },
  setAttribute: function setAttribute(tagName, value) {
    this[tagName] = value;
  },
};
/**
 * envNavigator
 */
var Navigator = function () {};
window.safeFunction(Navigator);
Object.defineProperties(Navigator.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "Navigator",
    configurable: true,
  },
});

Navigator.prototype.appCodeName = "Mozilla";
Navigator.prototype.appName = "Netscape";
Navigator.prototype.appVersion =
  "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36";
Navigator.prototype.cookieEnabled = true;
Navigator.prototype.deviceMemory = 8;
Navigator.prototype.doNotTrack = null;
Navigator.prototype.hardwareConcurrency = 8;
Navigator.prototype.language = "zh-CN";
Navigator.prototype.languages = ["zh-CN", "zh"];
Navigator.prototype.maxTouchPoints = 0;
Navigator.prototype.onLine = true;
Navigator.prototype.pdfViewerEnabled = true;
Navigator.prototype.platform = "MacIntel";
// navigator.plugins = new PluginArray();
Navigator.prototype.product = "Gecko";
Navigator.prototype.productSub = "20030107";
Navigator.prototype.userAgent =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36";
Navigator.prototype.vendor = "Google Inc.";
Navigator.prototype.vendorSub = "";
Navigator.prototype.webdriver = false;
plugins = [
  {
    description: "APlayer III ActiveX hosting plugin for Firefox",
    filename: "npaplayer.dll",
    length: 1,
    name: "APlayer ActiveX hosting plugin",
    type: "application/x-google-chrome-APlayer", //巨坑，一定需要带上这些！！！
    suffixes: "APlayer", //巨坑，一定需要带上这些！！！
  },
  {
    description: "ASUS Update",
    filename: "npAsusUpdate3.dll",
    length: 1,
    name: "ASUS Update",
    type: "application/x-google-chrome-ASUS", //巨坑，一定需要带上这些！！！
    suffixes: "ASUS", //巨坑，一定需要带上这些！！！
  },
  {
    description: "Portable Document Format",
    filename: "internal-pdf-viewer",
    length: 1,
    name: "Chrome PDF Plugin",
    type: "application/x-google-chrome-pdf", //巨坑，一定需要带上这些！！！
    suffixes: "pdf", //巨坑，一定需要带上这些！！！
  },
];

any_plugins = true;

if (any_plugins) {
  for (var i = 0; i < 10; i++) {
    var p = {
      description: randomString(parseInt(Math.random() * 20)),
      filename: randomString(parseInt(Math.random() * 20)) + ".dll",
      length: 1,
      name: randomString(parseInt(Math.random() * 10)),
      type: randomString(parseInt(Math.random() * 10)),
      suffixes: randomString(parseInt(Math.random() * 10)),
    };

    plugins.push(p);
  }
}
Navigator.prototype.plugins = plugins;
Navigator.prototype.mimeTypes = [
  {
    description: "Portable Document Format",
    type: "application/pdf",
    suffixes: "pdf",
    // enabledPlugin:[

    // ]
  },
  {
    description: "Portable Document Format",
    type: "pdf",
    suffixes: "pdf",
    // enabledPlugin:[

    // ]
  },
];

Navigator.prototype.clearAppBadge = function clearAppBadge() {};
window.safeFunction(Navigator.prototype.clearAppBadge);
Navigator.prototype.getBattery = function getBattery() {};
window.safeFunction(Navigator.prototype.getBattery);
Navigator.prototype.getGamepads = function getGamepads() {};
window.safeFunction(Navigator.prototype.getGamepads);
Navigator.prototype.getInstalledRelatedApps =
  function getInstalledRelatedApps() {};
window.safeFunction(Navigator.prototype.getInstalledRelatedApps);
Navigator.prototype.getUserMedia = function getUserMedia() {};
window.safeFunction(Navigator.prototype.getUserMedia);
Navigator.prototype.javaEnabled = function javaEnabled() {};
window.safeFunction(Navigator.prototype.javaEnabled);
Navigator.prototype.registerProtocolHandler =
  function registerProtocolHandler() {};
window.safeFunction(Navigator.prototype.registerProtocolHandler);
Navigator.prototype.requestMIDIAccess = function requestMIDIAccess() {};
window.safeFunction(Navigator.prototype.requestMIDIAccess);
Navigator.prototype.requestMediaKeySystemAccess =
  function requestMediaKeySystemAccess() {};
window.safeFunction(Navigator.prototype.requestMediaKeySystemAccess);
Navigator.prototype.sendBeacon = function sendBeacon() {};
window.safeFunction(Navigator.prototype.sendBeacon);
Navigator.prototype.setAppBadge = function setAppBadge() {};
window.safeFunction(Navigator.prototype.setAppBadge);
Navigator.prototype.unregisterProtocolHandler =
  function unregisterProtocolHandler() {};
window.safeFunction(Navigator.prototype.unregisterProtocolHandler);
Navigator.prototype.vibrate = function vibrate() {};
window.safeFunction(Navigator.prototype.vibrate);
Navigator.prototype.webkitGetUserMedia = function webkitGetUserMedia() {};
window.safeFunction(Navigator.prototype.webkitGetUserMedia);
var PluginArray = function () {
  return myElements["myPlugin"];
};
window.safeFunction(PluginArray);
Object.defineProperties(PluginArray.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "PluginArray",
    configurable: true,
  },
});
PluginArray.prototype.item = function item() {};
window.safeFunction(PluginArray.prototype.item);
PluginArray.prototype.namedItem = function namedItem() {};
window.safeFunction(PluginArray.prototype.namedItem);
PluginArray.prototype.refresh = function refresh() {};
window.safeFunction(PluginArray.prototype.refresh);
var navigator = new Navigator();

/**
 * envLocalStorage
 */
var Storage = function () {};
window.safeFunction(Storage);
Object.defineProperties(Storage.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "Storage",
    configurable: true,
  },
});
Storage.prototype.clear = function clear() {};
window.safeFunction(Storage.prototype.clear);
Storage.prototype.getItem = function getItem(tagName) {
  console.log("Storage.prototype.getItem->", tagName);
  return myElements["localStorage"][tagName];
};
window.safeFunction(Storage.prototype.getItem);
Storage.prototype.key = function key(index) {
  console.log("Storage.prototype.key", index);
};
window.safeFunction(Storage.prototype.key);
Storage.prototype.removeItem = function removeItem(tagName) {
  delete myElements.localStorage[tagName];
};
window.safeFunction(Storage.prototype.removeItem);
Storage.prototype.setItem = function setItem(tagName, value) {
  console.log("Storage.prototype.setItem->", value);
  debugger;
  if (tagName === "___ts___") {
  } else {
    myElements["localStorage"][tagName] = value;
  }
};
window.safeFunction(Storage.prototype.setItem);
// localStorage = new Storage();
localStorage = {
  getItem: function (key) {
    console.log("window.localStorage.getItem->", key);
    return this[key];
  },
  setItem: function (key, val) {
    console.log("window.localStorage.setItem->", key, val);
    this[key] = val;
  },
  removeItem: function (key) {
    delete this[key];
  },
};
window.sessionStorage = {
  getItem: function (key) {
    return this[key];
  },
  setItem: function (key, val) {
    this[key] = val;
  },
};
sessionStorage = new Storage();

var IDBFactory = function () {};
window.safeFunction(IDBFactory);
Object.defineProperties(IDBFactory.prototype, {
  constructor: {
    value: constructor,
    writable: true,
    configurable: true,
  },
  [Symbol.toStringTag]: {
    value: "IDBFactory",
    configurable: true,
  },
});
IDBFactory.prototype.cmp = function cmp() {};
window.safeFunction(IDBFactory.prototype.cmp);
IDBFactory.prototype.databases = function databases() {};
window.safeFunction(IDBFactory.prototype.databases);
IDBFactory.prototype.deleteDatabase = function deleteDatabase() {};
window.safeFunction(IDBFactory.prototype.deleteDatabase);
IDBFactory.prototype.open = function open() {};
window.safeFunction(IDBFactory.prototype.open);

/**
 * envWindow
 */
window.clearInterval = function clearInterval() {};
window.safeFunction(window.clearInterval);
window.clearTimeout = function clearTimeout() {};
window.safeFunction(window.clearTimeout);
window.clientInformation = navigator;
window.close = function close() {};
window.safeFunction(window.close);
window.confirm = function confirm() {};
window.safeFunction(window.confirm);
// window.cookieStore=function (){};
window.createImageBitmap = function createImageBitmap() {};
window.safeFunction(window.createImageBitmap);
// window.crypto=function crypto(){};
// window.customElements=function customElements(){};
// window.history=function (){};
window.innerHeight = 730;
window.innerWidth = 1536;
window.isSecureContext = true;
window.mainversion = 4;
window.name = "";
window.origin = document.origin;
window.originAgentCluster = false;
window.outerHeight = 40;
window.outerWidth = 252;
window.pageXOffset = 0;
window.pageYOffset = 0;
window.sitecode = "bm35000001";
window.setTimeout = function setTimeout(func, s) {
  // func();
};

window.location = location.prototype;
document.navigator = navigator;
document.localStorage = localStorage;

window.navigator = navigator;
window.addEventListener = EventTarget.prototype.addEventListener;
window.RegExp = RegExp;
window.setInterval = function setInterval(func, s) {
  // func()
};
window.Math = Math;
window.JSON = JSON;
window.parseFloat = parseFloat;
// window.localStorage = localStorage;
// window.sessionStorage = sessionStorage;
window.localStorage = localStorage;

window.document = document;
window.indexedDB = IDBFactory();
window.top = window;
window.self = window;
String.prototype.toLowerCase = function (data) {
  if (data) {
    return data.toLowerCase();
  } else {
    return null;
  }
};
// String.prototype.indexOf=function (data,key){
//   console.log(data,key);
//   if (data){
//     return data.indexOf(key);
//   }
// }
// console.log(window);

// function myProxy(obj) {
//   return new Proxy(obj, {
//     set(target, p, value, receiver) {
//       console.log("set:", p, value);
//       // console.log("set:", target, p, value);
//       // console.log(window.XMLHttpRequest.prototype.open)
//       return Reflect.set(...arguments);
//     },
//     get(target, p, receiver) {
//       console.log("get:", p);
//       // console.log("get:",target, p);
//       return target[p];
//     },
//   });
// }
// window = myProxy(window);
// window.location = myProxy(window.location);
// window.document = myProxy(window.document);
// window.navigator = myProxy(window.navigator);
// window.localStorage = myProxy(window.localStorage);
// window.sessionStorage = myProxy(window.sessionStorage);
// window.indexedDB = myProxy(window.indexedDB);
// window.performance = myProxy(window.performance);
// window.HTMLFormElement.prototype = myProxy(window.HTMLFormElement.prototype);
// window.HTMLAnchorElement= myProxy(window.HTMLAnchorElement);

// window.XMLHttpRequest.prototype=myProxy(window.XMLHttpRequest.prototype);
// window.document.location=myProxy(window.document.location);
// window.clientInformation=myProxy(window.clientInformation);
// window.Function=myProxy(window.Function);
// document=myProxy(document);