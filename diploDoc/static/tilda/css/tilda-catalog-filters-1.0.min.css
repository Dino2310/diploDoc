function t_store_filters_init(recid, options, data) {
    if (data.sort || data.search || data.filters && 0 !== data.filters.length) {
        var el_rec = document.getElementById("rec" + recid);
        el_rec.querySelectorAll(".js-store-filter").length > 0 || (t_store_filters_drawControls(recid, options, data),
        t_store_filters_showHideFilterControls(recid, el_rec),
        t_store_filters_handleOnChange(recid, options))
    }
}
function t_store_filters_showHideFilterControls(recid, el_rec) {
    window.addEventListener("click", (function(e) {
        var el_title = ""
          , clickedOnTitle = (e.target.classList.contains("js-store-filter-item-title") || e.target.closest(".js-store-filter-item-title")) && e.target.closest("#rec" + recid)
          , clickedInsideWrapper = e.target.classList.contains("js-store-filter-item-controls-wr") || e.target.closest(".js-store-filter-item-controls-wr");
        if (!clickedOnTitle)
            return clickedInsideWrapper ? void 0 : window.tStoreIsMobile ? void 0 : void Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-item"), (function(filterItem) {
                filterItem.classList.remove("active")
            }
            ));
        var el_item = (el_title = e.target).closest(".js-store-filter-item")
          , el_controlsWrap = el_item.querySelector(".js-store-filter-item-controls-wr");
        el_item.classList.contains("active") ? el_item.classList.remove("active") : (Array.prototype.forEach.call(document.querySelectorAll(".js-store-filter-item"), (function(filterItem) {
            filterItem.classList.remove("active")
        }
        )),
        el_item.classList.add("active"),
        el_controlsWrap.getBoundingClientRect().right + window.pageXOffset < 10 ? el_controlsWrap.classList.add("t-store__filter__item-controls-wrap_left") : el_controlsWrap.getBoundingClientRect().right + window.pageXOffset < 0 && console.log("controlsWrap offset right < 0"))
    }
    ))
}
function t_store_filters_drawControls(recid, options, data) {
    t_store_filters_cashSortOptsInData(data);
    var str = ""
      , searchSortStr = ""
      , isT1025 = "1025" === options.prodCard.blockId;
    searchSortStr += '<div class="t-store__filter__search-and-sort">',
    data.search && (searchSortStr += t_store_filters_drawControls_getSearchHtml()),
    data.sort && (searchSortStr += t_store_filters_drawControls_getSortHtml(data)),
    searchSortStr += "</div>";
    var filterClass = "t-store__filter js-store-filter";
    if (filterClass += options.isHorizOnMob ? " t-store__filter_horiz-on-mobile" : "",
    str += '<div class="' + (filterClass += isT1025 && options.colClassFullWidth ? " " + options.colClassFullWidth : "") + '">',
    str += '    <div class="t-store__filter__controls-wrapper">',
    str += "        " + t_store_filters_mobileBtns_getHtml(recid, data),
    str += "        " + t_store_filters_opts_getHtml(recid, data, options),
    !options.sidebar || window.innerWidth < 960)
        str += searchSortStr;
    else {
        var el_rec, el_sidebarBlock = (el_rec = document.getElementById("rec" + recid)).querySelector(".t951__cont-w-filter");
        el_sidebarBlock && el_sidebarBlock.insertAdjacentHTML("afterbegin", searchSortStr)
    }
    str += "    </div>";
    var choseBarStr = "";
    choseBarStr += '    <div class="t-store__filter__chosen-bar" style="display: none;">',
    choseBarStr += "    " + t_store_filters_opts_chosenVals_getHtml(),
    choseBarStr += "    " + t_store_filters_prodsNumber_getHtml(),
    choseBarStr += "    </div>",
    options.sidebar || (str += choseBarStr),
    str += "</div>";
    var el_rec, el_filterWrapper = (el_rec = document.getElementById("rec" + recid)).querySelector(".js-store-parts-select-container");
    if (t_store__removeElement(el_rec.querySelector(".js-store-filter")),
    el_filterWrapper)
        if (options.sidebar) {
            el_filterWrapper.insertAdjacentHTML("beforeend", choseBarStr);
            var t951Wrapper = el_filterWrapper.querySelector(".t951__sidebar-wrapper");
            t951Wrapper && t951Wrapper.insertAdjacentHTML("beforeend", str)
        } else
            el_filterWrapper.insertAdjacentHTML("beforeend", str);
    t_triggerEvent(el_rec, "controlsDrawn"),
    t_store_filters_opts_checkboxes_groupCheckedToHiddenInput(recid),
    t_store_filters_opts_customSelect_saveToHiddenInput(recid),
    t_store_filters_initUIBtnsOnMobile(el_rec),
    t_store_filters_initResetBtn(recid, options),
    t_store_filters_initExpandBtn(recid)
}
function t_store_filters_initResetBtn(recid, options) {
    var el_rec = document.getElementById("rec" + recid)
      , storeFilterReset = el_rec.querySelector(".js-store-filter-reset");
    storeFilterReset && storeFilterReset.addEventListener("click", (function() {
        Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-sort, .js-store-filter-opt"), (function(filter) {
            filter.value = ""
        }
        ));
        var search = el_rec.querySelector(".js-store-filter-search");
        search && (search.value = "",
        t_triggerEvent(search, "tstoreSearchTriggerReset")),
        Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-parts-switcher.t-active"), (function(switcher) {
            switcher.classList.remove("t-active")
        }
        ));
        var resetAll = el_rec.querySelector(".js-store-parts-switcher.t-store__parts-switch-btn-all");
        resetAll && resetAll.classList.add("t-active");
        var minPrice = ""
          , el_min = el_rec.querySelector(".js-store-filter-pricemin");
        el_min && (minPrice = t_store__getFormattedPrice(options, el_min.getAttribute("data-min-val")),
        el_min.value = minPrice);
        var el_max = el_rec.querySelector(".js-store-filter-pricemax")
          , maxPrice = "";
        if (el_max && (maxPrice = t_store__getFormattedPrice(options, el_max.getAttribute("data-max-val")),
        el_max.value = maxPrice),
        !options.defaultSort || options.defaultSort && !options.defaultSort.in_stock) {
            var onlyAvail = el_rec.querySelector(".js-store-filter-onlyavail");
            onlyAvail && (onlyAvail.checked = !1)
        }
        Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-opt-chb"), (function(item) {
            item.checked = !1
        }
        )),
        Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-custom-select.active, .t-store__filter__checkbox.active"), (function(item) {
            item.classList.remove("active")
        }
        )),
        el_min && el_min.setAttribute("data-previousmin", minPrice),
        el_max && el_max.setAttribute("data-previousmax", maxPrice);
        var storeFilterOpt = el_rec.querySelector(".t-store__filter__item_select .js-store-filter-opt");
        storeFilterOpt && storeFilterOpt.setAttribute("data-previousval", ""),
        el_rec.querySelector(".t-store__filter__chosen-bar").style.display = "none";
        var el_min_range = el_rec.querySelector(".t-store__filter__range_min")
          , el_max_range = el_rec.querySelector(".t-store__filter__range_max");
        options.sidebar && el_min_range && el_max_range && t_store_filters_updatePriceRange(el_rec),
        t_store_filters_send(recid, options),
        options.sidebar && (t_store_filters_opts_sort(options, recid),
        t_store_filters_scrollStickyBar(el_rec));
        var storeFilterChosenItem = el_rec.querySelectorAll(".js-store-filter-chosen-item");
        Array.prototype.forEach.call(storeFilterChosenItem, (function(item) {
            t_store__removeElement(item)
        }
        ));
        var storeFilterReset = el_rec.querySelector(".js-store-filter-reset");
        storeFilterReset && storeFilterReset.classList.remove("t-store__filter__reset_visible");
        var storeFilterSearchClose = el_rec.querySelector(".js-store-filter-search-close");
        storeFilterSearchClose && (storeFilterSearchClose.style.display = "none"),
        t_store_updateUrlWithParams("delete_all", null, null, recid)
    }
    ))
}
function t_store_filters_initExpandBtn(recid) {
    var el_rec, btnsExpanded = document.getElementById("rec" + recid).querySelectorAll(".js-store-filter-btn-expand");
    Array.prototype.forEach.call(btnsExpanded, (function(btn) {
        btn.addEventListener("click", (function() {
            var isExpanded = "no" !== this.getAttribute("data-expanded")
              , el_filters = this.parentNode.querySelector(".t-store__filter__item-controls-container")
              , button_text = this.querySelector(".t-store__filter__btn-text");
            if (isExpanded)
                Array.prototype.forEach.call(el_filters.querySelectorAll(".t-checkbox__control"), (function(control, i) {
                    i > 9 && control.classList.add("t-checkbox__control_hidden")
                }
                )),
                Array.prototype.forEach.call(el_filters.querySelectorAll(".t-store__filter__custom-sel"), (function(filter, i) {
                    i > 9 && filter.classList.add("t-store__filter__custom-sel_hidden")
                }
                )),
                button_text.textContent = window.tStoreDict["filter-expand"],
                el_filters.classList.remove("t-store__filter__item-controls-container_expanded"),
                this.setAttribute("data-expanded", "no");
            else {
                Array.prototype.forEach.call(el_filters.querySelectorAll(".t-checkbox__control_hidden"), (function(control) {
                    control.classList.remove("t-checkbox__control_hidden")
                }
                ));
                var storeFilterCustomSelHidden = el_filters.querySelector(".t-store__filter__custom-sel_hidden");
                storeFilterCustomSelHidden && storeFilterCustomSelHidden.classList.remove("t-store__filter__custom-sel_hidden"),
                button_text.textContent = window.tStoreDict["filter-collapse"],
                el_filters.classList.add("t-store__filter__item-controls-container_expanded"),
                this.setAttribute("data-expanded", "yes")
            }
        }
        ))
    }
    ))
}
function t_store_filters_cashSortOptsInData(data) {
    data.sortControlData = {
        name: "sort",
        label: window.tStoreDict["sort-label"],
        values: [{
            value: "",
            text: window.tStoreDict["sort-default"]
        }, {
            value: "price:asc",
            text: window.tStoreDict["sort-price-asc"]
        }, {
            value: "price:desc",
            text: window.tStoreDict["sort-price-desc"]
        }, {
            value: "title:asc",
            text: window.tStoreDict["sort-name-asc"]
        }, {
            value: "title:desc",
            text: window.tStoreDict["sort-name-desc"]
        }, {
            value: "created:desc",
            text: window.tStoreDict["sort-created-desc"]
        }, {
            value: "created:asc",
            text: window.tStoreDict["sort-created-asc"]
        }]
    }
}
function t_store_filters_drawControls_getSortHtml(data) {
    var str = "";
    str += '<div class="t-store__filter__sort">',
    str += '<div class="t-store__sort-select-wrapper">',
    str += '    <select class="t-store__sort-select t-descr t-descr_xxs js-store-filter-sort" name="sort">';
    for (var i = 0; i < data.sortControlData.values.length; i++) {
        var opt = data.sortControlData.values[i];
        str += '<option data-filter-value="' + opt.value + '" value="' + opt.value + '">' + opt.text + "</option>"
    }
    return str += "    </select>",
    str += "</div>",
    str += "</div>"
}
function t_store_filters_drawControls_getSearchHtml() {
    var str = "";
    return str += '<div class="t-store__filter__search t-descr t-descr_xxs">',
    str += '    <div class="t-store__search-wrapper">',
    str += '        <input class="t-store__filter__input js-store-filter-search" type="text" name="query" placeholder="' + window.tStoreDict.searchplaceholder + '">',
    str += '<svg class="t-store__search-icon js-store-filter-search-btn" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 88"> <path fill="#757575" d="M85 31.1c-.5-8.7-4.4-16.6-10.9-22.3C67.6 3 59.3 0 50.6.6c-8.7.5-16.7 4.4-22.5 11-11.2 12.7-10.7 31.7.6 43.9l-5.3 6.1-2.5-2.2-17.8 20 9 8.1 17.8-20.2-2.1-1.8 5.3-6.1c5.8 4.2 12.6 6.3 19.3 6.3 9 0 18-3.7 24.4-10.9 5.9-6.6 8.8-15 8.2-23.7zM72.4 50.8c-9.7 10.9-26.5 11.9-37.6 2.3-10.9-9.8-11.9-26.6-2.3-37.6 4.7-5.4 11.3-8.5 18.4-8.9h1.6c6.5 0 12.7 2.4 17.6 6.8 5.3 4.7 8.5 11.1 8.9 18.2.5 7-1.9 13.8-6.6 19.2z"></path></svg>',
    str += '<svg class="t-store__search-close-icon js-store-filter-search-close" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M0.781448 10.6465L10.7814 0.646484L11.4886 1.35359L1.48856 11.3536L0.781448 10.6465Z" fill="black"/><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6464 11.3536L0.646439 1.35359L1.35355 0.646484L11.3535 10.6465L10.6464 11.3536Z" fill="black"/></svg>',
    str += "    </div>",
    str += "</div>"
}
function t_store_filters_initUIBtnsOnMobile(el_rec) {
    var el_filtBtn = el_rec.querySelector(".js-store-filter-mob-btn")
      , el_filtOpts = el_rec.querySelector(".t-store__filter__options")
      , el_searchBtn = el_rec.querySelector(".js-store-search-mob-btn")
      , el_searchWrap = el_rec.querySelector(".t-store__filter__search-and-sort");
    el_filtBtn && el_filtBtn.addEventListener("click", (function() {
        el_searchWrap.style.display = "none",
        el_searchBtn && el_searchBtn.classList.remove("active"),
        el_filtBtn.classList.contains("active") ? (el_filtOpts.style.display = "",
        el_filtBtn.classList.remove("active")) : (el_filtOpts.style.display = "block",
        el_filtBtn.classList.add("active"))
    }
    )),
    el_searchBtn && el_searchBtn.addEventListener("click", (function() {
        el_filtBtn && el_filtBtn.classList.remove("active"),
        el_searchBtn.classList.contains("active") ? (el_searchWrap.style.display = "none",
        el_searchBtn.classList.remove("active")) : (el_searchWrap.style.display = "block",
        el_searchBtn.classList.add("active"))
    }
    ))
}
function t_store_filters_send(recid, options) {
    var filters = {}, el_rec = document.getElementById("rec" + recid), storeFilterPriceMin, checkedMinV, minVal, storeFilterPriceMax, checkedMaxV, maxVal;
    el_rec.querySelector(".js-store-filter-pricemin") && (minVal = t_store__cleanPrice(el_rec.querySelector(".js-store-filter-pricemin").getAttribute("data-min-val")),
    checkedMinV = t_store__cleanPrice(el_rec.querySelector(".js-store-filter-pricemin").value)),
    checkedMinV !== minVal && (filters["price:min"] = checkedMinV),
    el_rec.querySelector(".js-store-filter-pricemax") && (maxVal = t_store__cleanPrice(el_rec.querySelector(".js-store-filter-pricemax").getAttribute("data-max-val")),
    checkedMaxV = t_store__cleanPrice(el_rec.querySelector(".js-store-filter-pricemax").value)),
    checkedMaxV !== maxVal && (filters["price:max"] = checkedMaxV),
    el_rec.querySelector(".js-store-filter-onlyavail") && el_rec.querySelector(".js-store-filter-onlyavail").checked && (filters.quantity = "y");
    var params = window.tStoreCustomUrlParams;
    params && params[recid] && params[recid].quantity && "object" == typeof params[recid].quantity && "y" === params[recid].quantity[0] && (filters.quantity = "y");
    var storepartuid = el_rec.querySelector(".t-store__parts-switch-wrapper .js-store-parts-switcher.t-active:not(.t-store__parts-switch-btn-all)") || "";
    storepartuid && storepartuid.textContent && (filters.storepartuid = storepartuid.textContent),
    Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-opt"), (function(filterOpt) {
        var v = filterOpt.value
          , name = filterOpt.getAttribute("name");
        "sort" !== name && (v && "" !== v && "array" === filterOpt.getAttribute("data-info-type") ? filters[name] = v.split("&&") : v && (filters[name] = v))
    }
    ));
    var storeFilterSearch = el_rec.querySelector(".js-store-filter-search"), searchV;
    storeFilterSearch && (searchV = storeFilterSearch.value),
    searchV && (filters.query = searchV);
    var storeFilterSort = el_rec.querySelector(".js-store-filter-sort");
    if (storeFilterSort) {
        var sort = {}
          , sortV = storeFilterSort.value;
        if ("" === sortV && (sortV = el_rec.querySelector('.js-store-filter-opt[name="sort"]').value,
        t_store_isQueryInAddressBar("tfc_sort[" + recid + "]") && t_store_updateUrlWithParams("delete", "sort", ":", recid)),
        sortV) {
            var fieldName = sortV.split(":")[0]
              , sortDirection = sortV.split(":")[1];
            sort[fieldName] = sortDirection,
            t_store_updateUrlWithParams("update", "sort", fieldName + ":" + sortDirection, recid)
        }
        options.sort = sort
    }
    options.filters = filters,
    t_store_showLoadersForProductsList(recid, options),
    options.showPagination && "on" === options.showPagination && t_store_onFuncLoad("t_store_pagination_updateUrl", (function() {
        t_store_pagination_updateUrl(recid, 1)
    }
    )),
    t_store_loadProducts("", recid, options)
}
function t_store_filters_mobileBtns_getHtml(recid, data) {
    var str = "";
    return (data.filters.length > 0 || data.sort) && (str += '<div class="js-store-filter-mob-btn t-store__filter__opts-mob-btn t-name t-name_xs">',
    str += '<svg class="t-store__filter__opts-mob-btn-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 63.42 100"><defs><style>.cls-1{fill:#1d1d1b;}</style></defs><path class="cls-1" d="M13.75,22.59V.38h-6V22.59a10.75,10.75,0,0,0,0,20.64V99.62h6V43.23a10.75,10.75,0,0,0,0-20.64Z"/><path class="cls-1" d="M63.42,67.09a10.75,10.75,0,0,0-7.75-10.32V.38h-6V56.77a10.75,10.75,0,0,0,0,20.64V99.62h6V77.41A10.75,10.75,0,0,0,63.42,67.09Z"/></svg>',
    str += window.tStoreDict.filters,
    str += "</div>"),
    data.search && (str += '<div class="js-store-search-mob-btn t-store__filter__search-mob-btn t-descr t-descr_xs">',
    str += '<svg class="t-store__filter__search-mob-btn-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 88 88"> <path fill="#3f3f3f" d="M85 31.1c-.5-8.7-4.4-16.6-10.9-22.3C67.6 3 59.3 0 50.6.6c-8.7.5-16.7 4.4-22.5 11-11.2 12.7-10.7 31.7.6 43.9l-5.3 6.1-2.5-2.2-17.8 20 9 8.1 17.8-20.2-2.1-1.8 5.3-6.1c5.8 4.2 12.6 6.3 19.3 6.3 9 0 18-3.7 24.4-10.9 5.9-6.6 8.8-15 8.2-23.7zM72.4 50.8c-9.7 10.9-26.5 11.9-37.6 2.3-10.9-9.8-11.9-26.6-2.3-37.6 4.7-5.4 11.3-8.5 18.4-8.9h1.6c6.5 0 12.7 2.4 17.6 6.8 5.3 4.7 8.5 11.1 8.9 18.2.5 7-1.9 13.8-6.6 19.2z"></path></svg>',
    str += "</div>"),
    str
}
function t_store_filters_opts_getHtml(recid, data, opts) {
    var str = "";
    if (0 === data.filters.length && !data.sort)
        return "";
    str += '<div class="t-store__filter__options ' + (data.sort || data.search ? "" : "t-store__filter__options_center") + '">';
    var filtersArr = data.filters;
    data.sort && (str += t_store_filters_opts_getHtml_customSelect(data.sortControlData, opts)),
    opts.defaultSort && opts.defaultSort.in_stock && filtersArr.push({
        control: "checkbox",
        type: "product",
        name: "quantity",
        hidden: "y"
    });
    for (var i = 0; i < filtersArr.length; i++) {
        var f = filtersArr[i];
        "select" === f.control ? str += t_store_filters_opts_getHtml_customSelect(f, opts) : "checkbox" === f.control ? str += t_store_filters_opts_getHtml_checkbox(f, opts) : "range" === f.control && "price" === f.name && (str += t_store_filters_opts_getHtml_range(f, opts))
    }
    return str += "</div>"
}
function t_store_filters_opts_getOption(f) {
    var optionsData = t_store_option_getOptionsData();
    if (!optionsData)
        return null;
    var curOption = f.type && "option" === f.type ? optionsData[f.label] : null, isCustomOption;
    return curOption && t_store_option_checkIfCustom(curOption) ? curOption : null
}
function t_store_filters_opts_getHtml_customSelect(f, opts) {
    var str = ""
      , curOption = t_store_filters_opts_getOption(f);
    if (curOption && curOption.params && curOption.params.hasColor)
        return t_store_filters_opts_getHtml_checkbox(f, opts);
    var isColor, parentMod = "", itemsListMod = "";
    curOption && (parentMod = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__item"),
    itemsListMod = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__item-controls-container"),
    isColor = curOption.params && curOption.params.hasColor);
    var sortClass = "sort" === f.name ? "t-store__filter__item_sort-mobile" : "", customClass;
    str += '<div class="' + sortClass + " t-store__filter__item" + (curOption ? " t-store__filter__item_custom " : " ") + parentMod + ' t-store__filter__item_select js-store-filter-item t-descr t-descr_xxs">',
    str += '    <div class="t-store__filter__item-title js-store-filter-item-title" data-filter-name="' + f.name.toLowerCase() + '" ' + (f.label && f.label.length > 25 ? 'title="' + f.label + '"' : "") + ">" + f.label + "</div>",
    str += '    <div class="t-store__filter__item-controls-wrap js-store-filter-item-controls-wr">',
    str += '        <div class="t-store__filter__item-controls-container ' + itemsListMod + '" data-type="selectbox">',
    str += '        <input type="hidden" class="js-store-filter-opt" name="' + f.name + '">';
    var isExpandable = !1;
    if (f.values) {
        f.values = t_store_product_sortValues(f.values, "filter"),
        isExpandable = opts.sidebar && f.values.length > 10;
        for (var j = 0; j < f.values.length; j++) {
            var v = f.values[j].value
              , text = f.values[j].text
              , className = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__custom-sel");
            if (className = opts.sidebar && j > 9 ? className += " t-store__filter__custom-sel_hidden " : className += "",
            null != v) {
                var tmp = "", titleMod;
                if (tmp = '<div class="t-store__filter__custom-sel ' + className + " js-store-filter-custom-select " + sortClass + '" data-select-val="" data-filter-value="" type="selectbox">',
                isColor) {
                    var checkmarkStyle = curOption ? ' style="background-color: ' + t_store_option_getColorValue(curOption.values, v) + ';"' : "", checkmarkMod;
                    tmp += '<div class="t-store__filter__checkmark ' + t_store_option_getClassModificator(curOption, "filter", "t-store__filter__checkmark") + '"' + checkmarkStyle + "></div>"
                }
                tmp += '<div class="t-store__filter__title ' + t_store_option_getClassModificator(curOption, "filter", "t-store__filter__title") + '">' + (text || v) + "</div>",
                tmp += "    </div>";
                var el = document.createElement("div");
                el.innerHTML = tmp,
                el.children[0].setAttribute("data-select-val", v),
                el.children[0].setAttribute("data-filter-value", v),
                str += el.children[0].outerHTML
            }
        }
    }
    return str += "        </div>",
    isExpandable && (str += t_store_filters_opts_getHtml_expandButton()),
    str += "    </div>",
    str += "</div>"
}
function t_store_filters_opts_getHtml_checkbox(f, opts) {
    var str = "", curOption = t_store_filters_opts_getOption(f), isColor, isImage, parentMod = "", itemsListMod = "";
    curOption && (parentMod = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__item"),
    itemsListMod = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__item-controls-container"),
    isColor = curOption.params && curOption.params.hasColor,
    isImage = curOption.params && curOption.params.linkImage && !curOption.params.hasColor);
    var customClass = curOption ? " t-store__filter__item_custom " : " ";
    if ("quantity" === f.name)
        str += '<div class="t-store__filter__item t-store__filter__item_available js-store-filter-item t-descr t-descr_xxs"' + ("y" === f.hidden ? ' style="display:none;"' : "") + ">",
        str += '<div class="t-store__filter__item-title js-store-filter-item-title" data-filter-name="quantity" ' + (f.label && f.label.length > 25 ? 'title="' + f.label + '"' : "") + ">",
        str += f.label ? f.label : window.tStoreDict["filter-available-name"],
        str += "</div>",
        str += '<div class="t-store__filter__item-controls-wrap js-store-filter-item-controls-wr">',
        str += '<label class="t-checkbox__control t-descr t-descr_xxs">',
        str += '<input class="t-checkbox js-store-filter-onlyavail" type="checkbox" name="' + window.tStoreDict["filter-available-label"] + '" data-filter-value="' + window.tStoreDict["filter-available-label"] + '">',
        str += '<div class="t-checkbox__indicator"></div>',
        str += window.tStoreDict["filter-available-label"],
        str += "</label>",
        str += "</div>",
        str += "</div>";
    else {
        str += '<div class="t-store__filter__item ' + customClass + parentMod + ' t-store__filter__item_checkbox js-store-filter-item t-descr t-descr_xxs">',
        str += '    <div class="t-store__filter__item-title js-store-filter-item-title" data-filter-label="' + f.label.toLowerCase() + '" data-filter-name="' + f.name + '" ' + (f.label && f.label.length > 25 ? 'title="' + f.label + '"' : "") + ">" + f.label + "</div>",
        str += '    <div class="t-store__filter__item-controls-wrap js-store-filter-item-controls-wr">',
        str += '        <div class="t-store__filter__item-controls-container ' + itemsListMod + '" data-type="checkbox">',
        str += '            <input type="hidden" class="js-store-filter-opt" name="' + f.name + '" data-info-type="array">';
        var isExpandable = !1
          , isCheckmark = isColor || isImage;
        if (f.values) {
            f.values = t_store_product_sortValues(f.values, "filter"),
            isExpandable = opts.sidebar && f.values.length > 10;
            for (var j = 0; j < f.values.length; j++) {
                var v = f.values[j].value
                  , classes = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__checkbox");
                classes = opts.sidebar && j > 9 ? classes += " t-checkbox__control_hidden " : classes += "";
                var checkmarkMod = isCheckmark ? "t-store__filter__checkmark " + t_store_option_getClassModificator(curOption, "filter", "t-store__filter__checkmark") : "";
                if ("" !== v) {
                    var label = document.createElement("label");
                    label.classList.add("t-checkbox__control"),
                    label.classList.add("t-store__filter__checkbox"),
                    classes && classes.split(" ").forEach((function(className) {
                        "" !== className && label.classList.add(className)
                    }
                    )),
                    label.classList.add("t-descr"),
                    label.classList.add("t-descr_xxs");
                    var input = document.createElement("input");
                    input.classList.add("t-checkbox"),
                    input.classList.add("js-store-filter-opt-chb"),
                    input.setAttribute("type", "checkbox"),
                    input.setAttribute("name", t_store_unescapeHtml(v)),
                    input.setAttribute("data-filter-value", t_store_unescapeHtml(v)),
                    label.appendChild(input);
                    var div = document.createElement("div");
                    div.classList.add("t-checkbox__indicator"),
                    checkmarkMod && checkmarkMod.split(" ").forEach((function(className) {
                        "" !== className && div.classList.add(className)
                    }
                    )),
                    curOption && isColor && (div.style.backgroundColor = t_store_option_getColorValue(curOption.values, v)),
                    label.appendChild(div);
                    var span = document.createElement("span");
                    span.classList.add("t-store__filter__title");
                    var titleMod = t_store_option_getClassModificator(curOption, "filter", "t-store__filter__title");
                    titleMod && titleMod.split(" ").forEach((function(className) {
                        "" !== className && span.classList.add(className)
                    }
                    )),
                    span.appendChild(document.createTextNode(t_store_unescapeHtml(v))),
                    label.appendChild(span),
                    str += label.outerHTML
                }
            }
        }
        str += "        </div>",
        isExpandable && (str += t_store_filters_opts_getHtml_expandButton()),
        str += "    </div>",
        str += "</div>"
    }
    return str
}
function t_store_filters_opts_getHtml_range(f, options) {
    var isSliderAllowed = !window.tStoreIsIE
      , str = "";
    return str += '<div class="t-store__filter__item t-store__filter__item_price js-store-filter-item t-descr t-descr_xxs">',
    str += '    <div class="t-store__filter__item-title js-store-filter-item-title" ' + (f.label && f.label.length > 25 ? 'title="' + f.label + '"' : "") + ">",
    str += f.label ? f.label : window.tStoreDict["filter-price-name"],
    str += "    </div>",
    options.sidebar && isSliderAllowed && (str += t_store_filters_opts_getHtml_sliderRange(f)),
    str += '    <div class="t-store__filter__item-controls-wrap t-store__filter__item-price-box js-store-filter-item-controls-wr">',
    str += '        <input class="t-store__filter__input js-store-filter-pricemin" type="text" name="price:min" data-min-val="' + f.min + '" value="' + t_store__getFormattedPrice(options, f.min) + '">',
    str += '<span class="t-store__filter__delimeter">&nbsp;—&nbsp;</span><input class="t-store__filter__input js-store-filter-pricemax" type="text" name="price:max" data-max-val="' + f.max + '" value="' + t_store__getFormattedPrice(options, f.max) + '">',
    str += '<button class="t-store__filter__btn js-store-filter-price-btn">OK</button>',
    str += "    </div>",
    str += "</div>"
}
function t_store_filters_opts_getHtml_sliderRange(f) {
    var str = "";
    str += '<div class="t-store__filter__item-controls-wrap t-store__filter__item-price-slider js-store-filter-item-controls-wr">',
    str += '<div class="t-store__filter__price-outer t-store__filter__price-outer_start"></div>',
    str += '<div class="t-store__filter__price-outer t-store__filter__price-outer_end"></div>';
    var decimals = t_store_filters_price_countDecimals([f.min, f.max]), step;
    return step = 1 === decimals ? .1 : decimals >= 2 ? .01 : 1,
    str += '<input class="t-store__filter__range t-store__filter__range_min" type="range" name="price_range" min="' + t_store__cleanPrice(f.min) + '" max="' + t_store__cleanPrice(f.max) + '" step="' + step + '" data-min-val="' + t_store__cleanPrice(f.min) + '" value="' + t_store__cleanPrice(t_store__cleanPrice(f.min)) + '">',
    str += '<input class="t-store__filter__range t-store__filter__range_max" type="range" name="price_range" min="' + t_store__cleanPrice(f.min) + '" max="' + t_store__cleanPrice(f.max) + '" step="' + step + '" data-max-val="' + t_store__cleanPrice(f.max) + '" value="' + t_store__cleanPrice(f.max) + '">',
    str += '<div class="t-store__filter__range_bg"></div>',
    str += "</div>"
}
function t_store_filters_opts_checkboxes_groupCheckedToHiddenInput(recid) {
    var el_rec = document.getElementById("rec" + recid);
    Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-opt-chb"), (function(optChb) {
        optChb.addEventListener("change", (function() {
            t_store_filters_opts_checkboxes_changeHiddenInput(this)
        }
        ))
    }
    ))
}
function t_store_filters_opts_checkboxes_changeHiddenInput(el_changedCheckbox, fromSwitch) {
    var el_hiddenInput = el_changedCheckbox.closest(".js-store-filter-item").querySelector(".js-store-filter-opt")
      , value = el_hiddenInput.value;
    if (el_changedCheckbox.checked)
        fromSwitch ? value = el_changedCheckbox.getAttribute("name") : "" === value ? value = el_changedCheckbox.getAttribute("name") : value += "&&" + el_changedCheckbox.getAttribute("name");
    else {
        var arr = value.split("&&")
          , index = arr.indexOf(el_changedCheckbox.getAttribute("name"));
        -1 !== index && arr.splice(index, 1),
        value = arr.join("&&")
    }
    el_hiddenInput.value = value
}
function t_store_filters_opts_getHtml_expandButton() {
    var str = "";
    return str += '<button class="t-store__filter__btn-expand js-store-filter-btn-expand" data-expanded="no" type="button">',
    str += '<span class="t-store__filter__btn-text t-descr t-descr_xxs">' + window.tStoreDict["filter-expand"] + "</span>",
    str += "</button>"
}
function t_store_filters_opts_customSelect_saveToHiddenInput(recid) {
    var el_rec = document.getElementById("rec" + recid);
    Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-custom-select"), (function(customSelect) {
        customSelect.addEventListener("click", (function() {
            var el_hiddenInput = this.closest(".js-store-filter-item").querySelector(".js-store-filter-opt")
              , el_filterItem = this.closest(".js-store-filter-item");
            if (this.classList.contains("active"))
                return this.classList.remove("active"),
                void (el_hiddenInput.value = "");
            el_hiddenInput.value = this.getAttribute("data-select-val");
            var storeFilterCustomSelect = el_filterItem.querySelector(".js-store-filter-custom-select.active");
            storeFilterCustomSelect && storeFilterCustomSelect.classList.remove("active"),
            this.classList.add("active"),
            el_filterItem.classList.remove("active")
        }
        ))
    }
    ))
}
function t_store_filters_opts_customSelect_changeHiddenInput(element) {
    var el_hiddenInput = element.closest(".js-store-filter-item").querySelector(".js-store-filter-opt")
      , elementValue = element.getAttribute("data-select-val");
    el_hiddenInput.value = elementValue,
    el_hiddenInput.setAttribute("data-previousval", elementValue)
}
function t_store_filters_opts_chosenVals_getHtml() {
    var str = "";
    return str += '<div class="t-store__filter__chosen-wrapper js-store-opts-chosen-wrapper">',
    str += '<div class="t-store__filter__reset js-store-filter-reset t-descr t-descr_xxs">' + window.tStoreDict["filter-reset"] + "</div>",
    str += "</div>"
}
function t_store_filters_prodsNumber_getHtml() {
    var str = "";
    return str += '<div class="t-store__filter__prods-number js-store-filters-prodsnumber-wrap t-descr t-descr_xxs" style="display:none;">',
    str += window.tStoreDict["filter-prodsnumber"],
    str += ': <span class="js-store-filters-prodsnumber">',
    str += "</span>",
    str += "</div>"
}
function t_store_filters_prodsNumber_update(rec, options, obj) {
    if (options.filters) {
        var chosenBar = rec.querySelector(".t-store__filter__chosen-bar");
        chosenBar && (Object.keys(options.filters).length && options.previewmode && (!options.defaultSort || options.defaultSort && !options.defaultSort.in_stock) ? chosenBar.style.display = "" : chosenBar.style.display = "none");
        var changedFiltersNumber = Object.keys(options.filters).length
          , storeFiltersProdsNumberWrap = rec.querySelector(".js-store-filters-prodsnumber-wrap");
        if ((changedFiltersNumber > 1 || 1 === changedFiltersNumber && options.filters && (!options.defaultSort || options.defaultSort && !options.defaultSort.in_stock)) && obj && obj.products.length > 0 && options.isPublishedPage) {
            chosenBar && (chosenBar.style.display = "");
            var storeFiltersProdsNumber = rec.querySelector(".js-store-filters-prodsnumber");
            storeFiltersProdsNumber && (storeFiltersProdsNumber.textContent = obj.total),
            storeFiltersProdsNumberWrap && (storeFiltersProdsNumberWrap.style.display = "")
        } else {
            var chosenValues;
            if (storeFiltersProdsNumberWrap && (storeFiltersProdsNumberWrap.style.display = "none"),
            options.sidebar && chosenBar)
                chosenBar.querySelectorAll(".t-store__filter__chosen-val").length || (chosenBar.style.display = "none")
        }
    }
}
function t_store_filters_opts_chosenVal_add(recid, val, el_control, label) {
    if (el_control) {
        var container = el_control.closest(".t-store__filter__item-controls-container");
        if (container)
            var option = container.querySelector(".js-store-filter-opt").getAttribute("name")
    }
    "number" == typeof val && (val = val.toString());
    var valueForQuery = val.replace(/"/g, '\\"').replace(/\//g, "\\/");
    if (!document.getElementById("rec" + recid).querySelector('.t-store__filter__chosen-val[data-option-name="' + option + '"][data-field-val="' + valueForQuery + '"]')) {
        var el = document.createElement("div");
        el.classList.add("t-store__filter__chosen-val"),
        el.classList.add("js-store-filter-chosen-item"),
        el.classList.add("t-descr"),
        el.classList.add("t-descr_xxs"),
        el.setAttribute("data-field-val", val),
        option && el.setAttribute("data-option-name", option),
        el.appendChild(document.createTextNode(label ? t_store_unescapeHtml(label) : t_store_unescapeHtml(val)));
        var str = el.outerHTML, el_wrapper = document.getElementById("rec" + recid).querySelector(".js-store-opts-chosen-wrapper"), el_chosenTagItem;
        if (el_wrapper)
            el_wrapper.insertAdjacentHTML("afterbegin", str),
            (option ? el_wrapper.querySelector('.js-store-filter-chosen-item[data-field-val="' + valueForQuery + '"][data-option-name="' + option + '"]') : el_wrapper.querySelector('.js-store-filter-chosen-item[data-field-val="' + valueForQuery + '"]')) && (window.controlElem || (window.controlElem = {}),
            window.controlElem[recid] || (window.controlElem[recid] = {}),
            window.controlElem[recid][val] = el_control),
            el_wrapper.querySelectorAll(".js-store-filter-chosen-item").length > 1 && el_wrapper.querySelector(".js-store-filter-reset").classList.add("t-store__filter__reset_visible")
    }
}
function t_store_filters_handleOnChange(recid, options) {
    var el_rec = document.getElementById("rec" + recid);
    t_store_filters_handleOnChange_avail(recid, options, el_rec),
    t_store_filters_handleOnChange_price(recid, options, el_rec),
    options.sidebar && t_store_filters_handleOnChange_priceRange(options, el_rec),
    t_store_filters_handleOnChange_checkbox(recid, options, el_rec),
    t_store_filters_handleOnChange_selectbox(recid, options, el_rec),
    t_store_filters_handleOnChange_sort(recid, options, el_rec),
    t_store_filters_handleOnChange_search(recid, options, el_rec),
    t_store_filters_opts_checkedValues_hideOnClick(recid, options)
}
function t_store_filters_handleOnChange_avail(recid, options, el_rec) {
    var filterOnlyAvailable = el_rec.querySelector(".js-store-filter-onlyavail");
    filterOnlyAvailable && filterOnlyAvailable.addEventListener("change", (function() {
        var controlValue = this.getAttribute("name"), onlyAvailableControl, controlGroup;
        this.classList.contains("js-store-filter-onlyavail") && (controlValue = "y"),
        Array.prototype.forEach.call(this.closest(".t-store__filter__item-controls-wrap").parentNode.children, (function(sibling) {
            sibling.classList.contains("js-store-filter-item-title") && (controlGroup = sibling)
        }
        ));
        var controlGroupdId = controlGroup.getAttribute("data-filter-name");
        this.checked ? (t_store_updateUrlWithParams("add", controlGroupdId, controlValue, recid),
        t_store_filters_opts_chosenVal_add(recid, controlValue, this, window.tStoreDict["filter-available-label"])) : (t_store_updateUrlWithParams("delete", controlGroupdId, controlValue, recid),
        t_store_filters_opts_chosenVal_hide(el_rec, controlValue)),
        t_store_filters_send(recid, options)
    }
    ))
}
function t_store_filters_handleOnChange_price(recid, options, el_rec) {
    var el_priceFiltItem = el_rec.querySelector(".js-store-filter-item.t-store__filter__item_price"), el_min = el_rec.querySelector(".js-store-filter-pricemin"), el_max = el_rec.querySelector(".js-store-filter-pricemax"), minVal, maxVal;
    el_min && (minVal = t_store__cleanPrice(el_min.getAttribute("data-min-val"))),
    el_max && (maxVal = t_store__cleanPrice(el_max.getAttribute("data-max-val"))),
    el_min && !el_min.getAttribute("data-previousmin") && el_min.setAttribute("data-previousmin", minVal),
    options.sidebar && (el_min && el_min.addEventListener("change", (function() {
        var minPriceChanged, el_min_range;
        t_store_filters_handleOnChange_price_checkMin(recid, el_min, minVal, maxVal, options) && (t_store_filters_send(recid, options),
        t_triggerEvent(el_rec.querySelector(".t-store__filter__range_min"), "input"))
    }
    )),
    el_max && el_max.addEventListener("change", (function() {
        var maxPriceChanged, el_max_range;
        t_store_filters_handleOnChange_price_checkMax(recid, el_max, minVal, maxVal, options) && (t_store_filters_send(recid, options),
        t_triggerEvent(el_rec.querySelector(".t-store__filter__range_max"), "input"))
    }
    ))),
    el_min && Array.prototype.forEach.call(["keypress", "tstoreMinPriceTriggerReset"], (function(event) {
        el_min.addEventListener(event, (function(e) {
            if ("keypress" !== e.type || 13 === e.which) {
                var minPriceChanged = t_store_filters_handleOnChange_price_checkMin(recid, el_min, minVal, maxVal, options), maxPriceChanged = t_store_filters_handleOnChange_price_checkMax(recid, el_max, minVal, maxVal, options), isChanged;
                (minPriceChanged || maxPriceChanged) && (t_store_filters_send(recid, options),
                el_min.blur(),
                window.tStoreIsMobile || el_priceFiltItem.classList.remove("active"))
            }
        }
        ))
    }
    )),
    el_max && !el_max.getAttribute("data-previousmax") && el_max.setAttribute("data-previousmax", maxVal),
    el_max && Array.prototype.forEach.call(["keypress", "tstoreMaxPriceTriggerReset"], (function(event) {
        el_max.addEventListener(event, (function(e) {
            if ("keypress" !== e.type || 13 === e.which) {
                var minPriceChanged = t_store_filters_handleOnChange_price_checkMin(recid, el_min, minVal, maxVal, options), maxPriceChanged = t_store_filters_handleOnChange_price_checkMax(recid, el_max, minVal, maxVal, options), isChanged;
                (minPriceChanged || maxPriceChanged) && (t_store_filters_send(recid, options),
                el_max.blur(),
                window.tStoreIsMobile || el_priceFiltItem.classList.remove("active"))
            }
        }
        ))
    }
    ));
    var el_btn = el_rec.querySelector(".js-store-filter-price-btn");
    el_btn && el_btn.addEventListener("click", (function() {
        var minPriceChanged = t_store_filters_handleOnChange_price_checkMin(recid, el_min, minVal, maxVal, options), maxPriceChanged = t_store_filters_handleOnChange_price_checkMax(recid, el_max, minVal, maxVal, options), isChanged;
        (minPriceChanged || maxPriceChanged) && (t_store_filters_send(recid, options),
        window.tStoreIsMobile || el_priceFiltItem.classList.remove("active"))
    }
    ))
}
function t_store_filters_handleOnChange_priceRange(options, el_rec) {
    var isSliderAllowed = !window.tStoreIsIE;
    if (options.sidebar && isSliderAllowed) {
        var el_min_range = el_rec.querySelector(".t-store__filter__range_min"), el_max_range = el_rec.querySelector(".t-store__filter__range_max"), el_min_text = el_rec.querySelector(".js-store-filter-pricemin"), el_max_text = el_rec.querySelector(".js-store-filter-pricemax"), min, max, minRangeVal, maxRangeVal;
        el_min_text && (min = +el_min_text.getAttribute("data-min-val")),
        el_max_text && (max = +el_max_text.getAttribute("data-max-val")),
        el_min_range && (minRangeVal = t_store__cleanPrice(el_min_range.value)),
        el_max_range && (maxRangeVal = t_store__cleanPrice(el_max_range.value)),
        t_store_filters_calcPriceOuterWidth(el_rec, "start", min, max, minRangeVal),
        t_store_filters_calcPriceOuterWidth(el_rec, "end", min, max, maxRangeVal);
        var minTimer = null
          , maxTimer = null;
        el_min_range && el_min_range.addEventListener("input", (function() {
            var resultVal = t_store__cleanPrice(el_min_range.value)
              , minVal = t_store__cleanPrice(el_min_range.value)
              , maxVal = t_store__cleanPrice(el_max_range.value);
            min === max ? resultVal = max : minVal > maxVal ? resultVal = maxVal - 1 : minVal < min ? resultVal = min : minVal >= max && (resultVal = max - 1),
            el_min_range.value = resultVal;
            var formattedPrice = resultVal ? t_store__getFormattedPrice(options, resultVal.toString()) : resultVal;
            el_min_text.value = formattedPrice,
            t_store_filters_calcPriceOuterWidth(el_rec, "start", min, max, resultVal),
            minTimer && clearTimeout(minTimer),
            minTimer = setTimeout((function() {
                t_triggerEvent(el_min_text, "tstoreMinPriceTriggerReset"),
                t_store_filters_scrollStickyBar(el_rec)
            }
            ), 1e3)
        }
        )),
        el_max_range && el_max_range.addEventListener("input", (function() {
            var resultVal = t_store__cleanPrice(el_max_range.value)
              , minVal = t_store__cleanPrice(el_min_range.value)
              , maxVal = t_store__cleanPrice(el_max_range.value);
            min === max ? resultVal = max : maxVal < minVal ? resultVal = minVal + 1 : maxVal <= min ? resultVal = min + 1 : maxVal > max && (resultVal = max),
            el_max_range.value = resultVal;
            var formattedPrice = resultVal ? t_store__getFormattedPrice(options, resultVal.toString()) : resultVal;
            el_max_text.value = formattedPrice,
            t_store_filters_calcPriceOuterWidth(el_rec, "end", min, max, resultVal),
            maxTimer && clearTimeout(maxTimer),
            maxTimer = setTimeout((function() {
                t_triggerEvent(el_max_text, "tstoreMaxPriceTriggerReset"),
                t_store_filters_scrollStickyBar(el_rec)
            }
            ), 1e3)
        }
        ))
    }
}
function t_store_filters_handleOnChange_price_checkMax(recid, el_max, minVal, maxVal, options) {
    var el_rec = document.getElementById("rec" + recid)
      , val = t_store__cleanPrice(el_max.value);
    if (val.toString() !== el_max.getAttribute("data-previousmax").toString()) {
        var slider_el;
        if (val = t_store_filters_handleOnChange_checkInRange(val, el_max, minVal, maxVal, "max"),
        options && options.sidebar)
            el_rec.querySelector(".t-store__filter__range_max").value = val;
        var text = "< " + el_max.value;
        return el_max.getAttribute("data-previousmax") && t_store_filters_opts_chosenVal_hide(el_rec, el_max.getAttribute("data-previousmax")),
        val !== maxVal && t_store_filters_opts_chosenVal_add(recid, val, el_max, text),
        el_max.setAttribute("data-previousmax", val),
        val !== maxVal ? (el_max.setAttribute("data-filter-value", val),
        t_store_updateUrlWithParams("update", "price:max", val, recid)) : val <= maxVal && (el_max.setAttribute("data-filter-value", ""),
        t_store_updateUrlWithParams("delete", "price:max", val, recid)),
        !0
    }
    return !1
}
function t_store_filters_handleOnChange_price_checkMin(recid, el_min, minVal, maxVal, options) {
    var el_rec = document.getElementById("rec" + recid)
      , val = t_store__cleanPrice(el_min.value);
    if (val.toString() !== el_min.getAttribute("data-previousmin").toString()) {
        var slider_el;
        if (val = t_store_filters_handleOnChange_checkInRange(val, el_min, minVal, maxVal, "min"),
        options && options.sidebar)
            el_rec.querySelector(".t-store__filter__range_min").value = val;
        var text = "> " + el_min.value;
        return el_min.getAttribute("data-previousmin") && t_store_filters_opts_chosenVal_hide(el_rec, el_min.getAttribute("data-previousmin")),
        val !== minVal && t_store_filters_opts_chosenVal_add(recid, val, el_min, text),
        el_min.setAttribute("data-previousmin", val),
        val !== minVal ? (el_min.setAttribute("data-filter-value", val),
        t_store_updateUrlWithParams("update", "price:min", val, recid)) : val >= minVal && (el_min.setAttribute("data-filter-value", ""),
        t_store_updateUrlWithParams("delete", "price:min", val, recid)),
        !0
    }
    return !1
}
function t_store_filters_handleOnChange_checkInRange(val, el_input, minVal, maxVal, type) {
    return 0 === val && "max" === type ? (val = maxVal,
    el_input.value = maxVal) : val > maxVal ? (val = maxVal,
    el_input.value = maxVal) : val < minVal && (val = minVal,
    el_input.value = minVal),
    val
}
function t_store_filters_handleOnChange_checkbox(recid, options, el_rec) {
    Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-opt-chb"), (function(filterOptChb) {
        filterOptChb.addEventListener("change", (function() {
            var _this = this
              , controlValue = this.getAttribute("name")
              , childrensOfConstolsWrap = this.closest(".t-store__filter__item-controls-wrap").parentNode.children;
            Array.prototype.forEach.call(childrensOfConstolsWrap, (function(sibling) {
                if (sibling.classList.contains("js-store-filter-item-title")) {
                    var controlGroupdId = sibling.getAttribute("data-filter-name");
                    _this.checked ? (_this.parentNode.classList.add("active"),
                    t_store_updateUrlWithParams("add", controlGroupdId, controlValue, recid),
                    t_store_filters_opts_chosenVal_add(recid, controlValue, _this)) : (_this.parentNode.classList.remove("active"),
                    t_store_updateUrlWithParams("delete", controlGroupdId, controlValue, recid),
                    t_store_filters_opts_chosenVal_hide(el_rec, controlValue, _this)),
                    t_store_setActiveStorePart(recid),
                    t_store_filters_send(recid, options),
                    options.sidebar && (t_store_filters_opts_sort(options, recid),
                    t_store_filters_scrollStickyBar(el_rec))
                }
            }
            ))
        }
        ))
    }
    ))
}
function t_store_filters_handleOnChange_selectbox(recid, options, el_rec) {
    Array.prototype.forEach.call(el_rec.querySelectorAll(".js-store-filter-custom-select"), (function(filterCustomSelect) {
        filterCustomSelect.addEventListener("click", (function(e) {
            var isMobileSort = e.target.classList.contains("t-store__filter__item_sort-mobile") || this.classList.contains("t-store__filter__item_sort-mobile"), text = this.getAttribute("data-select-val"), label = this.textContent, controlGroup;
            Array.prototype.forEach.call(this.closest(".t-store__filter__item-controls-wrap").parentNode.children, (function(sibling) {
                sibling.classList.contains("js-store-filter-item-title") && (controlGroup = sibling)
            }
            ));
            var controlGroupdId = controlGroup.getAttribute("data-filter-name")
              , el_hiddenInput = this.closest(".js-store-filter-item").querySelector(".js-store-filter-opt")
              , previous = el_hiddenInput.getAttribute("data-previousval");
            if (previous && t_store_filters_opts_chosenVal_hide(el_rec, previous),
            previous === text)
                return t_store_updateUrlWithParams("delete", controlGroupdId, text, recid),
                t_store_setActiveStorePart(recid),
                t_store_filters_send(recid, options),
                el_hiddenInput.setAttribute("data-previousval", ""),
                void (options.sidebar && t_store_filters_opts_sort(options, recid));
            isMobileSort && (el_rec.querySelector(".js-store-filter-sort").value = text),
            t_store_updateUrlWithParams("update", controlGroupdId, text, recid),
            isMobileSort || t_store_filters_opts_chosenVal_add(recid, text, this, label),
            t_store_filters_send(recid, options),
            el_hiddenInput.setAttribute("data-previousval", text),
            options.sidebar && (t_store_filters_opts_sort(options, recid),
            t_store_filters_scrollStickyBar(el_rec))
        }
        ))
    }
    ))
}
function t_store_filters_handleOnChange_search(recid, options, el_rec) {
    var rec = document.getElementById("rec" + recid)
      , prevQuery = ""
      , el_input = el_rec.querySelector(".js-store-filter-search")
      , el_closeBtn = el_rec.querySelector(".js-store-filter-search-close")
      , el_searchBtn = el_rec.querySelector(".js-store-filter-search-btn")
      , params = window.tStoreCustomUrlParams;
    params && params[recid] && params[recid].query && "object" == typeof params[recid].query && (prevQuery = params[recid].query[0]),
    el_searchBtn && el_searchBtn.addEventListener("click", (function() {
        prevQuery !== el_input.value && (t_store_filters_opts_chosenVal_hide(el_rec, prevQuery),
        prevQuery = el_input.value,
        t_store_filters_handleOnChange_search_send(recid, el_input, el_closeBtn, options))
    }
    )),
    el_input && (Array.prototype.forEach.call(["keypress", "tstoreSearchTriggerReset"], (function name(event) {
        el_input.addEventListener(event, (function(e, value) {
            value && "" === prevQuery ? prevQuery = value : e.currentTarget.defaultValue && "" === prevQuery && (prevQuery = e.currentTarget.defaultValue,
            e.currentTarget.defaultValue = ""),
            "keypress" === e.type && 13 !== e.which || prevQuery !== el_input.value && (t_store_filters_opts_chosenVal_hide(el_rec, prevQuery),
            prevQuery = el_input.value,
            t_store_filters_handleOnChange_search_send(recid, el_input, el_closeBtn, options))
        }
        ))
    }
    )),
    el_input.addEventListener("keyup", (function() {
        this.value.length > 0 ? el_closeBtn.style.display = "" : 0 === this.value.length && (el_closeBtn.style.display = "none")
    }
    ))),
    el_closeBtn && el_closeBtn.addEventListener("click", (function() {
        rec.querySelector('.js-store-filter-search[name="query"]').getAttribute("value") && (prevQuery = rec.querySelector('.js-store-filter-search[name="query"]').getAttribute("value")),
        t_store_filters_opts_chosenVal_hide(el_rec, prevQuery),
        el_input.value = "",
        prevQuery = "",
        rec.querySelector('.js-store-filter-search[name="query"]').defaultValue = "",
        t_store_filters_handleOnChange_search_send(recid, el_input, el_closeBtn, options)
    }
    ))
}
function t_store_filters_handleOnChange_search_send(recid, el_input, el_closeBtn, options) {
    var val = el_input.value;
    if ("" !== val) {
        var chosenValText = window.tStoreDict.searchplaceholder + ": " + val;
        t_store_updateUrlWithParams("update", "query", val, recid),
        t_store_filters_opts_chosenVal_add(recid, val, el_input, chosenValText)
    } else
        el_closeBtn.style.display = "none",
        t_store_updateUrlWithParams("delete", "query", val, recid);
    t_store_filters_send(recid, options),
    el_input.blur()
}
function t_store_filters_handleOnChange_sort(recid, options, el_rec) {
    var storeFilterSort = el_rec.querySelector(".js-store-filter-sort");
    storeFilterSort && storeFilterSort.addEventListener("change", (function(e) {
        var selectedEl = this.querySelector('[selected="selected"]');
        selectedEl && (selectedEl.selected = !1),
        e.currentTarget && !document.documentMode && (e.currentTarget.selectedOptions[0].selected = !0),
        t_store_filters_send(recid, options)
    }
    ))
}
function t_store_filters_calcPriceOuterWidth(el_rec, endpoint, min, max, value) {
    var distance = max - min
      , isStart = "start" === endpoint
      , result = isStart ? Math.ceil((value - min) / distance * 100) : Math.ceil((max - value) / distance * 100);
    if (isStart) {
        var priceStart = el_rec.querySelector(".t-store__filter__price-outer_start");
        priceStart && (priceStart.style.width = result + "%")
    } else {
        var priceEnd = el_rec.querySelector(".t-store__filter__price-outer_end");
        priceEnd && (priceEnd.style.width = result + "%")
    }
}
function t_store_filters_updatePriceRange(el_rec) {
    var isSliderAllowed;
    if (!window.tStoreIsIE) {
        var el_min_range = el_rec.querySelector(".t-store__filter__range_min")
          , el_max_range = el_rec.querySelector(".t-store__filter__range_max")
          , el_min_text = el_rec.querySelector(".js-store-filter-pricemin")
          , el_max_text = el_rec.querySelector(".js-store-filter-pricemax");
        el_min_range && (el_min_range.value = t_store__cleanPrice(el_min_text.value),
        t_triggerEvent(el_min_range, "input")),
        el_max_range && (el_max_range.value = t_store__cleanPrice(el_max_text.value),
        t_triggerEvent(el_max_range, "input"))
    }
}
function t_store_filters_price_countDecimals(valuesArr) {
    for (var result = 0, i = 0; i < valuesArr.length; i++) {
        var number, numberAsString = (+valuesArr[i]).toString(), decimals = 0;
        -1 !== numberAsString.indexOf(".") && (decimals = numberAsString.split(".")[1].length),
        decimals > result && (result = decimals)
    }
    return result
}
function t_store_filters_opts_chosenVal_hide(el_rec, value, el_control) {
    var option = el_control && el_control.length ? el_control.closest(".t-store__filter__item-controls-container").querySelector(".js-store-filter-opt").getAttribute("name") : null;
    "number" == typeof value && (value = value.toString());
    var el_chosen = option ? el_rec.querySelector('.js-store-filter-chosen-item[data-field-val="' + value + '"][data-option-name="' + option + '"]') : el_rec.querySelector('.js-store-filter-chosen-item[data-field-val="' + value.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"]'), isSidebar;
    "951" === el_rec.getAttribute("data-record-type") && t_store_filters_updatePriceRange(el_rec);
    var el_min_range = el_rec.querySelector(".t-store__filter__range_min");
    if (el_min_range && t_triggerEvent(el_min_range, "input"),
    t_store__removeElement(el_chosen),
    el_rec.querySelectorAll(".js-store-filter-chosen-item").length <= 1) {
        var storeFilterReset = el_rec.querySelector(".js-store-filter-reset");
        storeFilterReset && storeFilterReset.classList.remove("t-store__filter__reset_visible")
    }
    if (0 === el_rec.querySelectorAll(".js-store-filter-chosen-item").length) {
        var storeFiltersProdsNumberWrap = el_rec.querySelector(".js-store-filters-prodsnumber-wrap");
        storeFiltersProdsNumberWrap && (storeFiltersProdsNumberWrap.style.display = "none");
        var chosenBar = el_rec.querySelector(".t-store__filter__chosen-bar");
        chosenBar && (chosenBar.style.display = "none")
    }
}
function t_store_filters_opts_checkedValues_hideOnClick(recid, options) {
    var el_rec = document.getElementById("rec" + recid), el_filterWrapper = el_rec.querySelector(".js-store-parts-select-container"), defVal;
    el_filterWrapper && el_filterWrapper.addEventListener("click", (function(e) {
        if (e.target.closest(".js-store-filter-chosen-item")) {
            var el_control = window.controlElem[recid][e.target.getAttribute("data-field-val")];
            if (!el_control)
                return e.target.textContent === window.tStoreDict["filter-available-label"] && (t_store_updateUrlWithParams("delete", "quantity", null, recid),
                t_store_filters_opts_chosenVal_hide(el_rec, "y", e.target),
                t_store_setActiveStorePart(recid),
                t_store_filters_send(recid, options),
                options.sidebar && (t_store_filters_opts_sort(options, recid),
                t_store_filters_scrollStickyBar(el_rec))),
                void console.log("smth wrong with current filter");
            el_control.classList.contains("js-store-filter-opt-chb") || el_control.classList.contains("js-store-filter-onlyavail") ? (el_control.checked = !1,
            t_triggerEvent(el_control, "change")) : el_control.classList.contains("js-store-filter-custom-select") ? el_control.click() : el_control.classList.contains("js-store-filter-pricemin") ? (defVal = t_store__getFormattedPrice(options, el_control.getAttribute("data-min-val")),
            el_control.value = defVal,
            t_triggerEvent(el_control, "tstoreMinPriceTriggerReset"),
            t_store_updateUrlWithParams("delete", "price:min", null, recid)) : el_control.classList.contains("js-store-filter-pricemax") ? (defVal = t_store__getFormattedPrice(options, el_control.getAttribute("data-max-val")),
            el_control.value = defVal,
            t_triggerEvent(el_control, "tstoreMaxPriceTriggerReset"),
            t_store_updateUrlWithParams("delete", "price:max", null, recid)) : el_control.classList.contains("js-store-filter-search") && (el_control.value = "",
            t_triggerEvent(el_control, "tstoreSearchTriggerReset"))
        }
    }
    ))
}
function t_store_filters_scrollStickyBar(el_rec) {
    var el_sidebar;
    el_rec.querySelector(".t951__sidebar") && ("scrollBehavior"in document.documentElement.style ? window.scrollTo({
        left: 0,
        top: el_rec.getBoundingClientRect().top + window.pageYOffset - 50,
        behavior: "smooth"
    }) : window.scrollTo(0, el_rec.getBoundingClientRect().top + window.pageYOffset - 50))
}
function t_store_filters_opts_sort(options, recid) {
    if (options.sidebar) {
        var el_rec, el_container = document.getElementById("rec" + recid).querySelectorAll(".t-store__filter__item-controls-container");
        Array.prototype.forEach.call(el_container, (function(control) {
            var type = control.getAttribute("data-type"), filterValues = [], el_controls;
            if ("checkbox" === type) {
                el_controls = control.querySelectorAll(".t-checkbox__control"),
                filterValues = [],
                Array.prototype.forEach.call(el_controls, (function(control) {
                    var value = control.querySelector(".js-store-filter-opt-chb").getAttribute("data-filter-value");
                    filterValues.push(value)
                }
                ));
                var arrayControls = Array.prototype.slice.call(el_controls, 0);
                Array.prototype.forEach.call(arrayControls, (function(sortedControl) {
                    var filterOptChb = sortedControl.getAttribute(".js-store-filter-opt-chb");
                    filterOptChb && filterOptChb.checked && sortedControl.classList.remove("t-checkbox__control_hidden"),
                    control.insertAdjacentElement("beforeend", sortedControl)
                }
                ))
            } else if ("selectbox" === type) {
                el_controls = control.querySelectorAll(".t-store__filter__custom-sel"),
                filterValues = [],
                Array.prototype.forEach.call(el_controls, (function(control) {
                    var value = control.getAttribute("data-filter-value");
                    filterValues.push(value)
                }
                ));
                var sortedActiveControls = Array.prototype.slice.call(el_controls, 0).sort((function(a, b) {
                    if (a.classList.contains("active") && b.classList.contains("active"))
                        return 1;
                    if (a.classList.contains("active") && !b.classList.contains("active"))
                        return -1;
                    if (!a.classList.contains("active") && !b.classList.contains("active")) {
                        var valueA = a.getAttribute("data-filter-value")
                          , valueB = b.getAttribute("data-filter-value")
                          , sorted = [valueA, valueB].sort();
                        return (sorted = t_store_product_sortValues(sorted, "string", filterValues)).indexOf(valueA) - sorted.indexOf(valueB)
                    }
                    return 0
                }
                ));
                Array.prototype.forEach.call(sortedActiveControls, (function(sortedControl) {
                    sortedControl.classList.contains("active") && sortedControl.classList.remove("t-store__filter__custom-sel_hidden"),
                    control.insertAdjacentElement("beforeend", sortedControl)
                }
                ))
            }
        }
        ))
    }
}
function t_store_filters_render_selected(options, recid) {
    try {
        var rec = document.getElementById("rec" + recid), filterObject = Object.assign({}, options.filters), sortObject = Object.assign({}, options.sort), controlType, el_control;
        for (var filterKey in filterObject)
            "string" == typeof filterObject[filterKey] && (filterObject[filterKey] = [filterObject[filterKey]]),
            filterObject[filterKey].forEach((function(filterValue) {
                var filterLabel;
                if (el_control = rec.querySelectorAll('[data-filter-value="' + filterValue.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"]'),
                "price:min" === filterKey)
                    (el_control = rec.querySelector('[name="price:min"]')).setAttribute("data-previousmin", parseInt(filterValue, 10)),
                    el_control.setAttribute("value", t_store__getFormattedPrice(options, filterValue)),
                    t_store_filters_opts_chosenVal_add(recid, filterValue, el_control, filterLabel = "> " + filterValue),
                    options.sidebar && (rec.querySelector(".t-store__filter__range_min").value = filterValue);
                else if ("price:max" === filterKey)
                    (el_control = rec.querySelector('[name="price:max"]')).setAttribute("data-previousmax", parseInt(filterValue, 10)),
                    el_control.setAttribute("value", t_store__getFormattedPrice(options, filterValue)),
                    t_store_filters_opts_chosenVal_add(recid, filterValue, el_control, filterLabel = "< " + filterValue),
                    options.sidebar && (rec.querySelector(".t-store__filter__range_max").value = filterValue);
                else if ("query" === filterKey)
                    rec.querySelector(".js-store-filter-search-close").style.display = "",
                    (el_control = rec.querySelector('[name="query"]')).setAttribute("value", filterValue),
                    el_control.value = filterValue,
                    filterLabel = window.tStoreDict.searchplaceholder + ": " + filterValue,
                    t_store_filters_opts_chosenVal_add(recid, filterValue, el_control, filterLabel);
                else if ("quantity" === filterKey)
                    (el_control = rec.querySelector(".js-store-filter-onlyavail")) && (el_control.checked = !0),
                    (!options.defaultSort || options.defaultSort && !options.defaultSort.in_stock) && (filterLabel = window.tStoreDict["filter-available-label"],
                    t_store_filters_opts_chosenVal_add(recid, filterValue, el_control, filterLabel));
                else if (el_control.length > 0)
                    switch (controlType = el_control[0].getAttribute("type")) {
                    case "checkbox":
                        Array.prototype.forEach.call(el_control, (function(control) {
                            var option = control.closest(".t-store__filter__item-controls-container").querySelector(".js-store-filter-opt").getAttribute("name"), isValid;
                            filterObject[option] && -1 !== filterObject[option].indexOf(filterValue) && (control.checked = !0,
                            control.parentNode.classList.add("active"),
                            t_store_filters_opts_chosenVal_add(recid, filterValue, control),
                            t_store_filters_opts_checkboxes_changeHiddenInput(control))
                        }
                        ));
                        break;
                    case "selectbox":
                        Array.prototype.forEach.call(el_control, (function(control) {
                            var option = control.closest(".t-store__filter__item-controls-container").querySelector(".js-store-filter-opt").getAttribute("name"), isValid;
                            filterObject[option] && -1 !== filterObject[option].indexOf(filterValue) && (t_store_filters_opts_chosenVal_add(recid, filterValue, control),
                            control.classList.add("active"),
                            t_store_filters_opts_customSelect_changeHiddenInput(control))
                        }
                        ))
                    }
            }
            ));
        for (var sortKey in sortObject) {
            var sortQuery = sortKey + ":" + sortObject[sortKey]
              , el_control_option = rec.querySelector('option[data-filter-value="' + sortQuery + '"]');
            el_control_option && (el_control_option.selected = !0);
            var el_control_select = rec.querySelector('.js-store-filter-custom-select[data-filter-value="' + sortQuery + '"]');
            el_control_select && el_control_select.classList.add("active")
        }
    } catch (e) {
        console.log("something wrong in t_store_filters_render_selected", e)
    }
}
function t_store_updateUrlWithParams(method, key, value, recid) {
    try {
        var params = window.tStoreCustomUrlParams || {};
        switch (params[recid] || (params[recid] = {}),
        value = (value || "").toString().replace(/&/g, "&amp;"),
        method) {
        case "add":
            params[recid][key] ? params[recid][key].push(value) : params[recid][key] = [value];
            break;
        case "update":
            params[recid][key] = [value];
            break;
        case "delete":
            if (!params[recid][key])
                break;
            var deleteThis;
            "string" == typeof params[recid][key] || "query" === key || "sort" === key || "price:min" === key || "price:max" === key || "quantity" === key ? delete params[recid][key] : params[recid][key] = params[recid][key].filter((function(item) {
                return item !== value
            }
            )),
            params[recid][key] && !params[recid][key].length && (params[recid][key] = null,
            delete params[recid][key]);
            break;
        case "delete_all":
            delete params[recid]
        }
        window.tStoreCustomUrlParams = params,
        t_store_paramsToObj_updateUrl(params)
    } catch (e) {
        console.log("something wrong in t_store_updateUrlWithParams", e)
    }
}
function t_store_addStoreParts(recid, options, storePartsArr) {
    var rec, el_store = document.getElementById("rec" + recid).querySelector(".js-store");
    options.storePartsArr = storePartsArr;
    var tabsHtml = t_store_get_storePartsControl_html(recid, options);
    el_store && (options.sidebar ? el_store.querySelector(".t951__sidebar-wrapper").insertAdjacentHTML("afterbegin", tabsHtml) : el_store.querySelector(".js-store-parts-select-container").insertAdjacentHTML("afterbegin", tabsHtml)),
    t_store_initStoreParts(recid, options)
}
function t_store_initStoreParts(recid, options) {
    var rec = document.getElementById("rec" + recid);
    Array.prototype.forEach.call(rec.querySelectorAll(".js-store-parts-switcher"), (function(switcher) {
        switcher.addEventListener("click", (function() {
            var params = window.tStoreCustomUrlParams || {}, el_hiddenInput, previousInputValue, prevControl, storeparttitle = this.textContent, activeBtn = rec.querySelector(".t-active");
            if (activeBtn && activeBtn.classList.remove("t-active"),
            this.classList.add("t-active"),
            options.filters || (options.filters = {}),
            this.classList.contains("t-store__parts-switch-btn-all"))
                options.filters.storepartuid && delete options.filters.storepartuid,
                params[recid] && params[recid].storepartuid && params[recid].storepartuid.forEach((function(storepart) {
                    var control = rec.querySelector('.js-store-filter-opt-chb[data-filter-value="' + storepart.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"]');
                    control && (control.checked = !1),
                    t_store_filters_opts_chosenVal_hide(rec, storepart)
                }
                )),
                (el_hiddenInput = rec.querySelector('.js-store-filter-opt[name="storepartuid"]')) && (el_hiddenInput.value = ""),
                params[recid] || (params[recid] = {}),
                params[recid].storepartuid = [],
                window.tStoreCustomUrlParams = params,
                t_store_updateUrlWithParams("delete", "storepartuid", storeparttitle, recid);
            else {
                if (options.filters.storepartuid = [storeparttitle],
                rec.querySelectorAll(".js-store-filter").length > 0) {
                    var controlType, el_control = rec.querySelector('[data-filter-value="' + storeparttitle.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"]');
                    if (el_control)
                        switch ((el_hiddenInput = el_control.closest(".js-store-filter-item").querySelector(".js-store-filter-opt")) && (previousInputValue = el_hiddenInput.value),
                        previousInputValue && ((prevControl = rec.querySelector('[data-filter-value="' + previousInputValue.replace(/"/g, '\\"') + '"]')).checked = !1,
                        prevControl.classList.remove("active"),
                        t_store_filters_opts_chosenVal_hide(rec, previousInputValue)),
                        controlType = el_control.getAttribute("type")) {
                        case "checkbox":
                            el_control.checked = !0,
                            t_store_filters_opts_chosenVal_add(recid, storeparttitle, el_control),
                            t_store_filters_opts_checkboxes_changeHiddenInput(el_control, !0);
                            break;
                        case "selectbox":
                            el_control.classList.add("active"),
                            t_store_filters_opts_chosenVal_add(recid, storeparttitle, el_control),
                            t_store_filters_opts_customSelect_changeHiddenInput(el_control)
                        }
                    else
                        (el_hiddenInput = rec.querySelector('.js-store-filter-opt[name="storepartuid"]')) && (previousInputValue = el_hiddenInput.value),
                        previousInputValue && ((prevControl = rec.querySelector('[data-filter-value="' + previousInputValue.replace(/"/g, '\\"') + '"]')).checked = !1,
                        prevControl.classList.remove("active"),
                        t_store_filters_opts_chosenVal_hide(rec, previousInputValue),
                        el_hiddenInput.value = "")
                }
                t_store_updateUrlWithParams("update", "storepartuid", storeparttitle, recid)
            }
            options.sidebar && t_store_filters_scrollStickyBar(rec),
            t_store_showLoadersForProductsList(recid, options),
            t_store_loadProducts("", recid, options),
            t_store_mobileHoriz_checkBtnVisibility(recid, options),
            t_store_setActiveStorePart(recid)
        }
        ))
    }
    ))
}
function t_store_showLoadersForProductsList(recid, options) {
    var rec = document.getElementById("rec" + recid);
    Array.prototype.forEach.call(rec.querySelectorAll(".t-store__card"), (function(card) {
        card.classList.add("t-store__card_hidden")
    }
    )),
    clearTimeout(rec.getAttribute("data-preloader-timeout"));
    var preloaderTimerId = setTimeout((function() {
        if (options && options.sidebar) {
            var t951GridContainer = rec.querySelector(".t951__grid-cont");
            t951GridContainer && t951GridContainer.classList.add("t951__grid-cont_hidden")
        } else
            rec.querySelector(".js-store-grid-cont").innerHTML = "";
        var gridPreloader = rec.querySelector(".js-store-grid-cont-preloader");
        gridPreloader.style.display = "",
        gridPreloader.style.opacity = 0,
        gridPreloader.style.transition = "opacity 200ms",
        gridPreloader.style.opacity = "1"
    }
    ), 1e3);
    rec.setAttribute("data-preloader-timeout", preloaderTimerId)
}
function t_store_setActiveStorePart(recid) {
    var rec = document.getElementById("rec" + recid)
      , params = window.tStoreCustomUrlParams
      , activeBtn = rec.querySelector(".t-active");
    activeBtn && activeBtn.classList.remove("t-active"),
    Array.prototype.forEach.call(rec.querySelectorAll(".js-store-parts-switcher"), (function(switcher) {
        var isAllButton = switcher.classList.contains("t-store__parts-switch-btn-all");
        if (params && params[recid]) {
            var partName = switcher.innerHTML
              , partNameDecode = switcher.innerHTML.replace(/&gt;/g, ">").replace(/&lt;/g, "<").replace(/&amp;/g, "&")
              , parts = params[recid].storepartuid;
            !parts || -1 === parts.indexOf(partName) && -1 === parts.indexOf(partNameDecode) || switcher.classList.add("t-active"),
            !parts && isAllButton && switcher.classList.add("t-active")
        } else
            isAllButton && switcher.classList.add("t-active")
    }
    ))
}
function t_store_get_storePartsControl_html(recid, options) {
    var str = "";
    str += '<div class="t-store__parts-switch-wrapper t-align_center">',
    str += '<div class="js-store-parts-switcher t-store__parts-switch-btn t-name t-name_xs t-menu__link-item t-store__parts-switch-btn-all" data-storepart-link="#!/tstore/r/' + recid + "/c/" + options.storepart + '" data-storepart-uid="' + options.storepart + '" >',
    str += window.tStoreDict.all,
    str += "</div>";
    for (var i = 0; i < options.storePartsArr.length; i++) {
        var storePart = options.storePartsArr[i];
        str += '<div class="js-store-parts-switcher t-store__parts-switch-btn t-name t-name_xs t-menu__link-item" data-storepart-link="#!/tstore/r/' + recid + "/c/" + storePart.uid + "-" + storePart.title + '" data-storepart-uid="' + storePart.uid + '">',
        str += "" + storePart.title,
        str += "</div>"
    }
    return str += "</div>"
}
function t_store_filters_getDictObj() {
    var dict = {
        filters: {
            EN: "Filters",
            RU: "Фильтры",
            FR: "Filtres",
            DE: "Filter",
            ES: "Filtros",
            PT: "Filtros",
            UK: "Фільтри",
            JA: "フィルター",
            ZH: "过滤器",
            PL: "Filtry",
            KK: "Сүзгілер",
            IT: "Filtri",
            LV: "Filtri"
        },
        searchplaceholder: {
            EN: "Search",
            RU: "Поиск",
            FR: "Recherche de produit",
            DE: "Produktsuche",
            ES: "Buscar productos",
            PT: "Procurar produtos",
            UK: "Пошук товарів",
            JA: "商品を探す",
            ZH: "搜索商品",
            PL: "Wyszukaj produkt",
            KK: "Іздеу",
            IT: "Ricerca",
            LV: "Meklēt"
        },
        "sort-label": {
            EN: "Sort",
            RU: "Сортировка",
            FR: "Trier",
            DE: "Sortieren nach",
            ES: "Ordenar",
            PT: "Ordenar",
            UK: "Сортування",
            JA: "並べ替え",
            ZH: "分类",
            PL: "Sortuj",
            KK: "Сорт",
            IT: "Ordina per",
            LV: "Šķirot"
        },
        "sort-default": {
            EN: "Sort: by default",
            RU: "Порядок: по умолчанию",
            FR: "Trier: par défaut",
            DE: "Sortieren nach: Standardmäßig",
            ES: "Ordenar: por defecto",
            PT: "Ordenar: por padrão",
            UK: "Сортування: за замовчуванням",
            JA: "並べ替え：デフォルトで",
            ZH: "分类: 默认",
            PL: "Sortuj: dowolnie",
            KK: "Сұрыптау: Әдепкі бойынша",
            IT: "Ordina: per impostazione predefinita",
            LV: "Kārtot: pēc noklusējuma"
        },
        "sort-price-asc": {
            EN: "Price: low to high",
            RU: "Цена: по возрастанию",
            FR: "Prix: par ordre croissant",
            DE: "Preis: aufsteigend",
            ES: "Precio: de más bajo a más alto",
            PT: "Preço: baixo para alto",
            UK: "Ціна: спочатку дешеві",
            JA: "価格の安い順番",
            ZH: "价格: 从便宜到贵",
            PL: "Cena: od najniższej",
            KK: "Бағасы: төменнен жоғары",
            IT: "Prezzo crescente",
            LV: "Cena: no zema uz augstu"
        },
        "sort-price-desc": {
            EN: "Price: high to low",
            RU: "Цена: по убыванию",
            FR: "Prix: par ordre décroissant",
            DE: "Preis: absteigend",
            ES: "Precio: de más alto a más bajo",
            PT: "Preço: alto para baixo",
            UK: "Ціна: спочатку дорогі ",
            JA: "価格の高い順番",
            ZH: "价格: 从贵到便宜",
            PL: "Cena: od najdroższej",
            KK: "Бағасы: жоғарыдан төмен",
            IT: "Prezzo decrescente",
            LV: "Cena: no augstākās līdz zemākajai"
        },
        "sort-name-asc": {
            EN: "Title: A—Z",
            RU: "Название: А—Я",
            FR: "Titre: A—Z",
            DE: "Titel: A—Z",
            ES: "Título: A—Z",
            PT: "Título: A—Z",
            UK: "Назва:  А—Я",
            JA: "製品名：五十音順",
            ZH: "商品名称: 字母顺序排列",
            PL: "Nazwa: A-Ż",
            KK: "Атауы: A-Z",
            IT: "Titolo: A-Z",
            LV: "Nosaukums: A-Z"
        },
        "sort-name-desc": {
            EN: "Title: Z—A",
            RU: "Название: Я—А",
            FR: "Titre: Z—A",
            DE: "Titel: Z—A",
            ES: "Título: Z—A",
            PT: "Título: Z—A",
            UK: "Назва: Я—А",
            JA: "製品名：降順",
            ZH: "商品名称: 降序母顺序排列",
            PL: "Nazwa: Ż-A",
            KK: "Атауы: Z-A",
            IT: "Titolo: Z-A",
            LV: "Nosaukums: no Z līdz A"
        },
        "sort-created-desc": {
            EN: "Sort: newest first",
            RU: "Порядок: сперва новые",
            FR: "Trier: le plus récent en premier",
            DE: "Sortieren nach: Neueste zuerst",
            ES: "Ordenar: más nuevos primero",
            PT: "Ordenar: mais recente primeiro",
            UK: "Сортування: спочатку нові",
            JA: "最新のものから並べ替え",
            ZH: "分类: 最新的",
            PL: "Sortuj: najnowsze",
            KK: "Сұрыптау: Бірінші жаңалар Бірінші",
            IT: "Nuovi primo",
            LV: "Kārtot: jaunākie vispirms"
        },
        "sort-created-asc": {
            EN: "Sort: oldest first",
            RU: "Порядок: сперва старые",
            FR: "Trier: le plus ancien en premier",
            DE: "Sortieren nach: Älteste zuerst",
            ES: "Ordenar: el más antiguo primero",
            PT: "Ordenar: mais antigo primeiro",
            UK: "Сортування: спочатку старі",
            JA: "並べ替え：古いものから",
            ZH: "分类: 最早的",
            PL: "Sortuj: najstarsze",
            KK: "Сұрыптау: көне бірінші",
            IT: "Ordina: prima i più vecchi",
            LV: "Kārtot: vecākie vispirms"
        },
        "filter-price-name": {
            EN: "Price",
            RU: "Цена",
            FR: "Prix",
            DE: "Preis",
            ES: "Precio",
            PT: "Preço",
            UK: "Ціна",
            JA: "価格",
            ZH: "价格",
            PL: "Cena",
            KK: "Баға",
            IT: "Prezzo",
            LV: "Cena"
        },
        "filter-available-name": {
            EN: "Availability",
            RU: "Наличие",
            FR: "Disponibilité",
            DE: "Verfügbarkeit",
            ES: "Disponibilidad",
            PT: "Disponibilidade",
            UK: "Наявність",
            JA: "可用性",
            ZH: "可用性",
            PL: "Dostępność",
            KK: "Болуы",
            IT: "Disponibilità",
            LV: "Pieejamība"
        },
        "filter-available-label": {
            EN: "Only in stock",
            RU: "Только товары в наличии",
            FR: "Seulement articles en stock",
            DE: "Nur auf Lager",
            ES: "Solo artículos en stock",
            PT: "Apenas itens em estoque",
            UK: "Тільки товари в наявності",
            JA: "在庫品のみ",
            ZH: "只有货",
            PL: "Tylko dostępne produkty",
            KK: "Тек қоймада",
            IT: "Solo in magazzino",
            LV: "Tikai noliktavā"
        },
        "filter-reset": {
            EN: "Clear all",
            RU: "Очистить все",
            FR: "Tout effacer",
            DE: "Alles löschen",
            ES: "Limpiar todo",
            PT: "Limpar tudo",
            UK: "Очистити все",
            JA: "すべてクリア",
            ZH: "全部清除",
            PL: "Wyczyść wszystko",
            KK: "Барлығын тазалау",
            IT: "Cancella tutto",
            LV: "Nodzēst visu"
        },
        "filter-expand": {
            EN: "Show all",
            RU: "Показать все",
            FR: "Afficher tout",
            DE: "Alles anzeigen",
            ES: "Mostrar todo",
            PT: "Mostrar tudo",
            UK: "Показати все",
            JA: "すべて表示",
            ZH: "显示全部",
            PL: "Pokaż wszystko",
            KK: "Барлығын көрсету",
            IT: "Mostra tutto",
            LV: "Rādīt visu"
        },
        "filter-collapse": {
            EN: "Collapse",
            RU: "Свернуть",
            FR: "Réduire",
            DE: "Einklappen",
            ES: "Colapsar",
            PT: "Colapsar",
            UK: "Згорнути",
            JA: "折りたたむ",
            ZH: "收起",
            PL: "Zwiń",
            KK: "Тасалау",
            IT: "Riduci",
            LV: "Sakļaut"
        },
        "filter-prodsnumber": {
            EN: "Found",
            RU: "Найдено",
            FR: "Trouvé",
            DE: "Gefunden",
            ES: "Encontrado",
            PT: "Encontrado",
            UK: "Знайдено",
            JA: "見つかった",
            ZH: "发现",
            PL: "Znaleziono",
            KK: "Табылған",
            IT: "Trovato",
            LV: "Atrasts"
        }
    }
      , lang = window.tStoreBrowserLang;
    window.tStoreDict || (window.tStoreDict = {}),
    Object.keys(dict).forEach((function(key) {
        window.tStoreDict[key] = dict[key][lang] ? dict[key][lang] : dict[key].EN
    }
    ))
}
function t_triggerEvent(el, eventName) {
    var event;
    document.createEvent ? (event = document.createEvent("HTMLEvents")).initEvent(eventName, !0, !1) : document.createEventObject && ((event = document.createEventObject()).eventType = eventName),
    event.eventName = eventName,
    el.dispatchEvent ? el.dispatchEvent(event) : el.fireEvent ? el.fireEvent("on" + event.eventType, event) : el[eventName] ? el[eventName]() : el["on" + eventName] && el["on" + eventName]()
}
window.tStoreIsIE = !!document.documentMode,
t_onReady((function() {
    t_store_filters_getDictObj()
}
)),
window.tStoreIsIE && "function" != typeof Object.assign && Object.defineProperty(Object, "assign", {
    value: function assign(target) {
        "use strict";
        if (!target)
            throw new TypeError("Cannot convert undefined or null to object");
        for (var to = Object(target), index = 1; index < arguments.length; index++) {
            var nextSource = arguments[index];
            if (nextSource)
                for (var nextKey in nextSource)
                    Object.prototype.hasOwnProperty.call(nextSource, nextKey) && (to[nextKey] = nextSource[nextKey])
        }
        return to
    },
    writable: !0,
    configurable: !0
});
