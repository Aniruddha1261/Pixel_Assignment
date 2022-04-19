/*
For Search.pl: suggestion dropdown box 
*/
function seeAll(){
	var name = document.getElementById('name_choice');
	var req = name.value;
	if(name.value.indexOf('\(') != -1){									
		req = name.value.substring(0, name.value.indexOf('\(') - 1 );
	}	
	window.open('search.pl?query=' + req);
}
/*****************/
var lastselection = 'active';
var lastcontent = null;

function clickactive() {
	if (lastselection != 'active') {
		var tmp = document.getElementById('infocontent').innerHTML;
		document.getElementById('infocontent').innerHTML = lastcontent;
		lastcontent = tmp; 
		lastselection = 'active';
		document.getElementById('menuiteminfo').className = '';
		document.getElementById('menuitemgeneral').className = 'active';
	}
}

function clickinfo() {
	if (lastselection != 'info') {
		var tmp = document.getElementById('infocontent').innerHTML;
		document.getElementById('infocontent').innerHTML = lastcontent;
		document.getElementById('menuiteminfo').className = 'active';
		document.getElementById('menuitemgeneral').className = '';
		lastcontent = tmp;
		lastselection = 'info';
	}
}

function details(command)
{
        var wait = 'Retrieving information, please wait ...';
	if (lastselection != 'info') {
		lastcontent = wait;
		document.getElementById('menuiteminfo').style.visibility = 'visible';
		clickinfo();
	} else {
		document.getElementById('infocontent').innerHTML = wait;
	}
        /*
         * if get info of gene: get ref_neighbor gene id
         */
        var comms = command.split(":");
        if(comms[0].indexOf("gene") > -1){
            id = comms[1];
            homo_grp = document.getElementById(id).parentNode;
            ref_id = homo_grp.className.baseVal.split(" ")[1];
            command += ":" + ref_id;
        }
        document.getElementById('infocontent').innerHTML = retrInfo(command);
}

/*
For phyloview, CNE track: when mouseover the CNE, it highlights the target genes
*/
function cne_mouseover(targets)
{
	var n = targets.split(";");
	for(var i = 0; i < n.length - 1; i++){
		document.getElementById(n[i]).setAttribute('fill-opacity','1');
		document.getElementById(n[i]).setAttribute('stroke-width','2');
		document.getElementById(n[i]).setAttribute('stroke-opacity', '1');
	}
}

function cne_mouseout(targets)
{
	var n = targets.split(";");
	for(var i = 0; i < n.length - 1; i++){
		document.getElementById(n[i]).removeAttribute('fill-opacity');
		document.getElementById(n[i]).removeAttribute('stroke-width');
		document.getElementById(n[i]).removeAttribute('stroke-opacity');
	}
}

/**********
 *  phyloview: display species to choose **/
showsidebar = false;
$(function(){
$('#toggle').click(function(){
	if(showsidebar == true){
		$('#leftpanelphylo').animate({width:0});
		$("div[id^='dv']").css("display", "none");
		$('#refreshSpec').css("display", "none");
		$('#leftpanelphylohide').animate({left:70});		
		showsidebar = false;
		$(this).attr("src", "../img/arrow_show.jpg");
	}
	else{
		$(this).attr("src", "../img/arrow_hide.jpg")
		$('#leftpanelphylo').animate({width:325});
		$('#leftpanelphylohide').animate({left:395});
		$("input[id^='morecheckdv']").each(function(){
			if($(this).val() == 'hide'){
				$(this).parent().next().css("display", "block");
			}
		})
		$('#refreshSpec').css("display", "block");
		showsidebar = true;
	}
});
});

function checkboxSpec(id){
	var checkbox = document.getElementById(id);
	var checkbut = document.getElementById('morecheck'+id);
	if(checkbox.style.display == 'none'){
		checkbox.style.display = 'block';
		checkbut.value = 'hide';
	}else{
		checkbox.style.display = 'none';
		checkbut.value = 'more';
	}
}

function partialcheck(id){
	document.getElementById(id).indeterminate = true;
}

$(window).load(function(){
	var check =	document.getElementsByClassName("indeterminate");		
	for(var i = 0; i < check.length; i++){
		check[i].indeterminate = true;
		check[i].checked = true;
	}
	
	$("input[id^='ancestral']:checked").each(function(){
		$("#allcheckances").prop("indeterminate", true);
		$("#allcheckances").prop("checked", true);
	});
	
	$("input[id^='group']:checked").each(function(){
		$("#allcheck").prop("indeterminate", true);
		$("#allcheck").prop("checked", true);
	});
	
	
});

/**
 * Refresh button
 */
function refresh(){
    var url = String(window.location);
    var param = "";
    $("input:checkbox[name=species]:checked").each(function() {
       	param += $(this).attr("id") + ":";
    }); 
    
    url = removeURLParameter(url, "xhide");
    url = removeURLParameter(url, "xcollapse");
    url = removeURLParameter(url, "mhide");
    url = removeURLParameter(url, "mshow");
    url = removeURLParameter(url, "showonly");
    url = removeURLParameter(url, "clickshow");
    url = removeURLParameter(url, "clickhide");

    if(param != '') url += "&amp;showonly="+param;
    else if(param == '' && url.indexOf("phyloview_size") != -1){
        url += "&amp;blank=1";
    }

    window.open(url, "_self");
}

contextisvisible = 0;

/*
For phyloview and alignview: context-menu (right-click) for navigating to matrix view and karyoview
*/
/* show construction graph */

function show_graph(id, species_name, gene_name){
    if(species_name == "Homo/Pan group"){ species_name = "HomoPan";}
    elem = document.getElementById(id);
    var html = "<iframe src='/preview/" + species_name + "/" + gene_name + "/'></iframe><br/>";
    $("#showGraphPopup").html(html);
    $("#showGraphPopup").dialog({width:'680px',height:'auto',modal:false, buttons: [
            {text: "Detail", 
                click: function(){
                    url = "/graphs/" + species_name + "/" + gene_name + "/graph-denovo/4";
                    window.open(url, "_blank");}
            },
            {text: "Close",
                click: function() {
                $(this).dialog("close");}
            }  ],
            position: {my : "right top", at: "right bottom", of: elem, collision: "fit"},
    });
    $(".ui-dialog-titlebar").hide();
}

function rightClick(spec_id)
{
	var species = document.getElementsByClassName('speciesname');
		var ancestral = document.getElementsByClassName('ancestralname');
		if (species || ancestral)
		{
	    	for (var i = 0; i < species.length + ancestral.length; i++)
	    	{
	    		var element = (i < species.length) ? species[i] : ancestral[i-species.length];
	        	element.addEventListener('contextmenu', function(event)
	        	{
	        		text='<ul><li><a href=\"karyoview.pl?species_id1='+ spec_id + '&amp;species_id2=' + this.id +'\" target=\"_blank\">Karyotype View</a></li><li><a href=\"karyoview.pl?view=0&amp;species_id1=' + spec_id + '&amp;species_id2=' + this.id +'\" target=\"_blank\">Matrix View</a></li><li><a href=\"phyldiag_handle.pl?species_id1=' + spec_id + '&amp;species_id2=' + this.id +'\" target=\"_blank\">Phyldiag View</a></li></ul>'
	        		el=document.getElementById('context_menu')
					contextisvisible=1
					el.innerHTML=text
					el.style.visibility='visible'
					e=event?event:window.event
					el.style.left=pageXOffset+e.clientX+'px'
					el.style.top=pageYOffset+e.clientY+'px'
					e.preventDefault()
					return false
	        	}, true);
		    }
		}
	}



/**
 * Select node to hide/show from phylo tree
 */
function selectToHide(id, choice){
    mode = (id.indexOf("hide") != -1) ? "hide" : "show";
    node = document.getElementById(id);
    hide = ":" + id.replace(new RegExp(mode, "g"), "");
    switch(choice){
        case 1: // click to select or deselect
            if(mode == "hide"){
                cross = node.previousSibling;
                while(cross && cross.nodeType != 1){
                    cross = cross.previousSibling;
                }
                line = cross.previousSibling;
                while(line && line.nodeType != 1){
                    line = line.previousSibling;
                }
                if(node.style.stroke != ""){
                    node.removeAttribute("style");
                    cross.removeAttribute("style");
                    line.removeAttribute("style");
                }
                else{
                    cross.style.display = "inline";
                    node.style.stroke = "orange";
                    node.style.fill = "orange";
                    line.style.stroke = "orange";
                }
            }
            else{
                line = node.previousSibling;
                while(line && line.nodeType != 1){
                    line = line.previousSibling;
                }

                if(node.style.fill != ""){
                    node.removeAttribute("style");
                    line.removeAttribute("style");
                }
                else{
                    node.style.fill = "orange";
                    line.style.stroke = "orange";
                }
            }
            break;
        case 2: // 
            if(mode == "show"){
                node.removeAttribute("style");
                line = node.previousSibling;
                while(line && line.nodeType != 1){
                    line = line.previousSibling;
                }
                line.removeAttribute("style");
            }
            break;
        case 3: // Click to show or remove lines
            nodes = (mode == "hide") ? getElementsByClassName(document, "hidenode") : getElementsByClassName(document, "shownode");
            toremove = (mode == "hide") ? getURLParameter("clickshow") : getURLParameter("clickhide");
            //remove id of current element
            toremove = toremove.replace(new RegExp(hide, "g"), "");
            
            for ( i = 0; i < nodes.length; i++){
                nodei = document.getElementById(nodes[i].id);
                if(nodei != null){
                    x = String(nodes[i].id).replace(new RegExp(mode, "g"), "").trim();
                    if(nodes[i].id != id && nodei.style.fill != ""){
                        hide += ":" + x;
                        toremove = toremove.replace(new RegExp(":"+x, "g"), "");
                    }
                }
            }
            url = String(window.location);
            oldhide = (mode == "hide") ? getURLParameter("clickhide") : getURLParameter("clickshow");
            if(oldhide != "null")
                hide += oldhide;
            
            url = (mode == "hide") ? removeURLParameter(url, "clickshow") : removeURLParameter(url,"clickhide");
            if(toremove != "null" && toremove != "")
                url += (mode == "hide") ? "&clickshow=" + toremove : "&clickhide=" + toremove;
            
            url = (mode == "hide") ? removeURLParameter(url, "clickhide") : removeURLParameter(url, "clickshow");
            url += (mode == "hide") ? "&clickhide=" + hide : "&clickshow=" + hide;

            window.open(url,"_self");
            
            break;
    }
}

/*
 * For phyloview: select CNE by score
*/
$(document).ready( function() {
     scores = getElementsByClassName(document, "Min S");
     for(i = 0; i < scores.length; i++){
        document.getElementById(scores[i].id).addEventListener("keydown", function(e){
            if(e.keyCode == 13){
                var minscores = getElementsByClassName(document, "Min S");
                var score = "";
                for (i=0; i < minscores.length; i++){
                    if(minscores[i].id == 1) score += minscores[i].value + ":";
                    else if(minscores[i].id == 2) score += minscores[i].value;
                }
                url = String(window.location);
                url = removeURLParameter(url, "score");
                if(score != ":"){
                    url = removeURLParameter(url, "track_cne");
                    url += "&amp;score=" + score + "&amp;track_cne=4";
                }
                window.open(url, '_self');
            }
        }, false);
     }
})

/*
 * For phyloviewsize
 */
function testphylo(id, mode){
    grp = getElementsByClassName(document, id);
    for(i = 0; i < grp.length; i++){
        if(mode == 1){
            grp[i].setAttribute("fill-opacity","1");
            grp[i].setAttribute("stroke-opacity","1");
            grp[i].setAttribute("stroke-width","2");
        }
        else{
            grp[i].removeAttribute("fill-opacity");
            grp[i].removeAttribute("stroke-opacity");
            grp[i].removeAttribute("stroke-width");
        }
    }
}

/*
 * For View Panel
 */
function dndsview(check,url_new){
    var url = window.location.href;
    var view = $('input[name=dnds_prot]:checked').val();
    //"unchecked"
    if(check == 1){
        if(view == 'cne'){
            url_new = removeURLParameter(url,'track_cne');
        }else{
            url_new = removeURLParameter(url,'dnds_view');
        }
    }else{
        if(view == "cne"){
            url_new = removeURLParameter(url, 'dnds_view');
            url_new = removeURLParameter(url_new, 'track_cne');
            url_new += "&track_cne=0";
        }
    }
    if(url_new != url){ window.open(url_new, '_self'); }
}

/****************
For Karyoview: when hover over the color legend, the correspond chromosome is hovered too
*/
var numNode = 0;

function highlightMe(chrom){
	var elements = getElementsByClassName(document, "chromtext"), n = elements.length;
	var elementsHomo = getElementsByClassName(document,"homology_group"), n_homo = elementsHomo.length;
	var meTxt = document.getElementById("text" + chrom);
	
        var fillcolor = rgbToHex(meTxt.style.fill);

	if(fillcolor == 'black' || fillcolor == '#000000' || fillcolor == '#0'){
		meTxt.style.fill = 'orange';
		numNode += 1;
		for(var i = 0; i < n; i++){
			var e = elements[i];
			var id = e.id.replace("text","");
		}
		/*turn off hover*/
		for(var j = 0; j < n_homo; j++){
			var el = elementsHomo[j];
                        
			if(el.id.indexOf("tmp") == -1) el.id = el.id + "tmp";
		}
	}
	/*deselect*/
	else{
		meTxt.style.fill = 'black';
		numNode -= 1;
	}
	
	/*deselect all, turn on hover*/
	if(numNode == 0){
		for(var i = 0; i < n; i++){
			var e = elements[i];
			var id = e.id.replace("text","");
                        e.style.fill = 'black';
		}
		for(var j = 0; j < n_homo; j++){
			var el = elementsHomo[j];
			if(el.id.indexOf('tmp') != -1) el.id = el.id.replace("tmp","");
		}
	}
}

/*
Right click on chromosome to choose hide chromosome or view chromosome in matrix view 
*/
function karyo_rightclick(){
	var chromtexts = getElementsByClassName(document,"chromtext");
	for (var i = 0; i < chromtexts.length; i++)
	{
		var element = chromtexts[i];
	     element.addEventListener('contextmenu', function(event)
	        	{
	        		chrom1 = this.id.replace("text","")
	        		chrom2 = this.getAttribute("name")
	        		text="<ul><li><a onclick=\"karyo_viewchrom(1," + chrom1 + ",'" + chrom2 + "')\">Matrix view of Chromosome</a></li>";
	        		text += "<li><a onclick=\"karyo_viewchrom(2," + chrom1 + ",'" + chrom2 + "')\">Hide Chromosome(s)</a></li>";
	        		text += "<li><a onclick=\"karyo_viewchrom(3," + chrom1 + ",'" + chrom2 + "')\">Hide Others</a></li>";
	        		text += "<li><a onclick=\"karyo_viewchrom(4," + chrom1 + ",'" + chrom2 + "')\">Show all</a></li>";
	        		text += "<li><a onclick=\"karyo_viewchrom(5," + chrom1 + ",'" + chrom2 + "')\">Deselect all</a></li></ul>";
	        		
	        		el=document.getElementById('context_menu')
					contextisvisible=1
					el.innerHTML=text
					el.style.visibility='visible'
					e=event?event:window.event
					el.style.left=pageXOffset+e.clientX+'px'
					el.style.top=pageYOffset+e.clientY+'px'
					e.preventDefault()
	        	}, true);
	}
}

function karyo_viewchrom(mode, chrom1, chrom2){
	var elements = getElementsByClassName(document, "chromtext"), n = elements.length;
	
	var url = String(window.location);
	var hide = getURLParameter("hide1");
        if (hide == "null") hide = "";
	var chrom = ":" + getURLParameter("chrom1");
	
	var str = chrom1 + ":"; // string of chosen chroms
	var choose = new Array(); // array of chosen chroms
        choose[0] = chrom1;
	var j = 1;

        var chrom2_multi = chrom2; // list (string) of chromosome 2 correspond with chosen chroms
	for(var i = 0; i < n; i++){
                var fillcolor = rgbToHex(elements[i].style.fill);
		if(fillcolor == 'orange' || fillcolor == '#ffa500'){
                        var id = elements[i].id.replace("text", "");
			if( id != chrom1){
				str += id + ":";
				choose[j++] = id;

                                chrom2_multi += elements[i].getAttribute("name");
			}
		}
	}
	
	switch(mode){
		case 1: /*view in matrix view*/
                        url = removeURLParameter(url, "view");
                        url += "&view=0";
                        
                        url = removeURLParameter(url, "chrom1");
			url = removeURLParameter(url, "chrom2");
			
                        url += "&chrom1=" + str + "&chrom2=" + chrom2_multi;
			break;
		case 2: /*hide chroms*/
                        url = removeURLParameter(url, "hide1");
                        url += "&hide1=" + hide + str;

			if(chrom != ':null'){
				var newchrom = chrom;
				for(var i = 0; i < choose.length; i++){
					if(chrom.indexOf(":"+choose[i] +":") != -1) { 
                                            newchrom = newchrom.replace(":"+choose[i]+":", ":");
                                        }
				}
                                newchrom = newchrom.replace(/^:+/g, '');
                                url = removeURLParameter(url, "chrom1");
                                url += "&chrom1=" + newchrom;
			}
			break;
		case 3:/*hide others*/
                        url = removeURLParameter(url, "chrom1");
                        url += "&chrom1=" + str;
			
                        url = removeURLParameter(url, "hide1");
			break;
		case 4:/*show all*/
                        url = removeURLParameter(url, "hide1");
                        url = removeURLParameter(url, "hide2");
                        url = removeURLParameter(url, "chrom1");
                        url = removeURLParameter(url, "chrom2");
			break;
		case 5:/*deselect all*/
			var elementsHomo = getElementsByClassName(document,"homology_group"), n_homo = elementsHomo.length;
			for(var i =0; i < n; i++){
				var e = elements[i];
				var id = e.id.replace("text","");
				
				e.style.fill = 'black';
			}
			for(var j = 0; j < n_homo; j++){
				var el = elementsHomo[j];
				if(el.id.indexOf('tmp') != -1) el.id = el.id.replace("tmp","");
			}
			return;
	}
	var idlist = document.getElementById('idlist').className;
        if(idlist != ''){ 
            url = removeURLParameter(url, "idlist");
            url += "&idlist=" + idlist;
        }
	window.open(url,'_self');
}

/**
 * mouseover color to highlight chromosome
 */
function hoverin(el, chromgrp){
	var elements = getElementsByClassName(document,"homology_group"), n = elements.length;
	for(var i = 0; i < n; i++){
		var e = elements[i];
		if(e.id.indexOf("tmp") == -1 && e.id != chromgrp) 
			e.style.display = "none";
                else if( e.id.indexOf("tmp") != -1){
                    if(el == "color"){
                        if(e.id != chromgrp+"tmp")
                            e.style.display = "none";
                    }
                }
	}
}
/**
 * mouseout color
 */
function hoverout(chromgrp){
	var elements = getElementsByClassName(document,"homology_group"), n = elements.length;
	for(var i = 0; i < n; i++){
		var e = elements[i];
		e.style.display = "block";
	}
}

/*
Right click on chromosome to hide or show chromosomes
*/
function matrix_rightclick(){
	var chromboxes1 = document.getElementsByClassName('chrombox1');
        var chromboxes2 = document.getElementsByClassName('chrombox2');
	for (var i = 0; i < chromboxes1.length + chromboxes2.length; i++)
	{
		var element;
                if(i < chromboxes1.length) element= chromboxes1[i];
                else element = chromboxes2[i-chromboxes1.length];
	        element.addEventListener('contextmenu', function(event)
	        	{
	        		id = this.id.split(":");
	        		text = "<ul><li><a onclick='hideChrom(" + id[0] + "," + id[1] + ",1)'>Hide Chromosome(s)</a></li>";
                                text += "<li><a onclick='hideChrom(" + id[0] + "," + id[1] + ",2)'>Hide Others</a></li>"; 
                                text += "<li><a onclick='hideChrom(" + id[0] + "," + id[1] + ",3)'>Show all</a></li>"; 
                                text += "<li><a onclick='hideChrom(" + id[0] + "," + id[1] + ",4)'>Deselect all</a></li></ul>"
	        		el=document.getElementById('context_menu')
					contextisvisible=1
					el.innerHTML=text
					el.style.visibility='visible'
					e=event?event:window.event
					el.style.left=pageXOffset+e.clientX+'px'
					el.style.top=pageYOffset+e.clientY+'px'
					e.preventDefault()
	        	}, true);
	}
}

function hideChrom(sp, id, mode){
    /**
     * sp: species id
     * id: chrombox id = [chromosome_id]
     */
	var url = String(window.location);

	var chromboxes = [getElementsByClassName(document, "chrombox1"), getElementsByClassName(document, "chrombox2")];

	var str = ["", ""];
	var choose = [new Array(), new Array()];
	var hide = [getURLParameter("hide1"), getURLParameter("hide2")];

	var chrom = [":" + getURLParameter("chrom1"), ":" + getURLParameter("chrom2")];

	for(var k = 0; k < 2; k++){
            var numChoose = 0;
            var j = 0;
	    for(var i = 0; i < chromboxes[k].length; i++){
                var fillcolor = rgbToHex(chromboxes[k][i].style.fill);
	    	if(fillcolor == 'orange' || fillcolor == '#ffa500'){
	    	    numChoose++;	
                    var chromboxid = chromboxes[k][i].id.split(":");
	    	    str[k] += chromboxid[1] + ":" ; 
	    	    choose[k][j++] = chromboxid[1];
	    	}
	    }
	    if( numChoose == 0 && k == (sp-1) ){ str[k] = id; }
            switch(mode){
	    	case 1: /* Hide chroms */
                    if(str[k] != ""){
                        url = removeURLParameter(url, "hide" + (k+1));
                        new_hide = (hide[k] == "null") ? str[k] : hide[k] + str[k];
                        url += "&hide" + (k+1) + "=" + new_hide;

	    		if(chrom[k] != ':null'){
	    			var newchrom = chrom[k];
	    			for(var i = 0; i < choose[k].length; i++){
	    				if(chrom[k].indexOf(":" + choose[k][i]) + ":" != -1) newchrom = newchrom.replace(":"+choose[k][i]+":", ":");
	    			}
                                newchrom = newchrom.replace(/^:+/g, '');
                                url = removeURLParameter(url, "chrom" + (k+1) );
                                url += "&chrom" + (k+1) + "=" + newchrom;
	    		}
                    }
	    		break;
	    	case 2: /* Hide others */
                    if(str[k] != ""){ 
                        url = removeURLParameter(url, "chrom" + (k+1));
                        url += "&chrom" + (k+1) + "=" + str[k];
                        url = removeURLParameter(url, "hide" + (k+1));
                    }
                        break;
	    	case 3: /* Show all */
                        if(k == sp - 1){
                            url = removeURLParameter(url, "hide" + (k+1));
                            url = removeURLParameter(url, "chrom" + (k+1));
                        }
	    		break;
	    	case 4: /* Deselect all*/
                        if(k == sp - 1){
	    		    for(var i = 0; i < chromboxes[k].length; i++){
	    		    	var e = chromboxes[k][i];
                                var fillcolor = rgbToHex(e.style.fill);
	    		    	if(fillcolor == 'orange' || fillcolor == '#ffa500'){
	    		    		e.style.fill = 'black';
	    		    	}
	    		    }
                        }
	    		break;
            }
        }
        if(mode == 4) return;
	window.open(url, "_self");
}

/*
 * Karyoview: choose chromosomes: check to choose or un-choose
 */
function checkChr(sp, chromid){
	var id = sp + ":" + chromid;
	var el = document.getElementById(id);
        var fillcolor = rgbToHex(el.style.fill);
	if(fillcolor == 'black' || fillcolor == '#000000' || fillcolor == "#0")
		el.style.fill = 'orange';
	else
		el.style.fill = 'black';
}

/*
 * For contextmenu: hide menu when user clicks elsewhere
 */
function hidemenu(){
	if (typeof el!="undefined" && contextisvisible){
		el.style.visibility="hidden"
		contextisvisible=0
	}
}

document.addEventListener("click", hidemenu, true)

/*
For karyo and matrix view: toggle the more option in sorting chromosomes and filtering by the chromosome's minsize
*/
function sortChrom(sort){
        var url = window.location.href;
        
	var lengthsort = [ document.getElementById('both_l'), document.getElementById('g1_l'), document.getElementById('g2_l')] ;
	var sizesort = [ document.getElementById('both_s'), document.getElementById('g1_s'), document.getElementById('g2_s')] ;
	for( var i = 0; i < lengthsort.length; i++){
		sizesort[i].checked = false;
		lengthsort[i].checked = false;
	}
        
        url = removeURLParameter(url, "sortsize");
        url = removeURLParameter(url, "sortlength");
    
        url = removeURLParameter(url, "sort");
        url += "&sort=" + sort;
        
        if(url.indexOf("species_id") != -1){
            window.open(url, "_self");
        }
}

function changeminkaryo(){
    var length = document.getElementById('lengthmore');
    var minsize = document.getElementById('minsize').value;
    var minnumK = document.getElementById('minnumK').value;

    if (length.style.display=='none'){
        document.getElementById('minsize2').value = minsize;
        document.getElementById('minnumK2').value = minnumK;
    }
}

function moreoption(){
        // div
        var length = document.getElementById('lengthmore');
	var sortlength = document.getElementById('sortlengthmore');
	// var
        var sortBut1 = document.getElementById('sortButt1');
	var sortBut2 = document.getElementById('sortButt2');
	
	var minsize2 = document.getElementById('minsize2');
	var minnumK2 = document.getElementById('minnumK2');
	
	var lengthsort = [ document.getElementById('both_l'), document.getElementById('g1_l'), document.getElementById('g2_l')] ;
	var sizesort = [ document.getElementById('both_s'), document.getElementById('g1_s'), document.getElementById('g2_s')] ;
	
	var lengthsort_param = "";
	var sizesort_param = "";
	var sort_param = "";
	
	var query = window.location.search.substring(1);
	var vars = query.split("&");
	for(var i = 0; i < vars.length; i++){
		var pair = vars[i].split("=");
		if(pair[0] == "sortlength"){
			lengthsort_param = pair[1];
		}else if(pair[0] == "sortsize"){
			sizesort_param = pair[1];
		} else if(pair[0] == "sort") {
			sort_param = pair[1];
		}
	}
		
	if(length.style.display=='none'){
		if(minsize2.value == ''){
			minsize2.value = document.getElementById('minsize').value;
		}
		if(minnumK2.value == ''){
			minnumK2.value = document.getElementById('minnumK').value;
		}
		length.style.display='inline';
		sortlength.style.display='inline';
		
		if(lengthsort_param == "" && sizesort_param == ""){
			if(sortBut1.checked == true) sizesort[0].checked = true;
			else if (sortBut2.checked == true) lengthsort[0].checked = true;
		}else{
		 	if(lengthsort_param != ""){
				if(lengthsort_param == "g1_l"){ lengthsort[1].checked = true;}
				else if(lengthsort_param == "g2_l") lengthsort[2].checked = true;
				else if(lengthsort_param == "both_l") lengthsort[0].checked = true;
			}
			if(sizesort_param != ""){
				if(sizesort_param == "g1_s"){ sizesort[1].checked = true;}
				else if(sizesort_param == "g2_s") sizesort[2].checked = true;
				else if(sizesort_param == "both_s") sizesort[0].checked = true;
			}
		}
		sortBut1.checked = false;
		sortBut2.checked = false;
                document.getElementById("moreopt").value = 1;
		
	}else if(length.style.display=='inline'){
		length.style.display='none';
		sortlength.style.display='none';
                document.getElementById("moreopt").value = 0;
	}
	
	if(sort_param == "length" || lengthsort_param == "both_l") sortBut2.checked = true;
	else if(sort_param == "size" || sizesort_param == "both_s") sortBut1.checked = true;
	
	form = document.getElementById('frm');
	species_id1 = form.species_choice1.selectedIndex;
	species_name1 = form.species_choice1.options[species_id1].value;
	species_id2 = form.species_choice2.selectedIndex;
	species_name2 = form.species_choice2.options[species_id2].value;
	if(species_name1 == species_name2){ minnumK2.disabled = true; minsize2.disabled = true;}
	else{ minnumK2.disabled = false; minsize2.disabled = false; }
}

function disableradio(radio){
	var lengthsort = [ document.getElementById('both_l'), document.getElementById('g1_l'), document.getElementById('g2_l')] ;
	var sizesort = [ document.getElementById('both_s'), document.getElementById('g1_s'), document.getElementById('g2_s')] ;
	var sortBut1 = document.getElementById('sortButt1'); //length
	var sortBut2 = document.getElementById('sortButt2'); //size

	if(radio == lengthsort[0]){ /*sort by length for both*/
		for( var i = 0; i < sizesort.length; i++){
			sizesort[i].checked = false;
		}
                sortBut2.checked = false;
                sortBut1.checked = false;
	}
	if(radio == sizesort[0]){
		for( var i = 0; i < lengthsort.length; i++){
			lengthsort[i].checked = false;
		}
                sortBut1.checked = false;
                sortBut2.checked = false;
	}
	
	for( var i = 1; i < lengthsort.length; i++){
		if(radio == lengthsort[i]){
			sizesort[i].checked = false;
			sizesort[0].checked = false;
                        sortBut2.checked = false;
                        sortBut1.checked = false;
		}   
	}
	
	for( var i = 1; i < sizesort.length; i++){
		if(radio == sizesort[i]){
			lengthsort[i].checked = false;
			lengthsort[0].checked = false;
                        sortBut1.checked = false;
                        sortBut2.checked = false;
		}
	}
}

/******************* Utilities *****************/
function file(fichier)
{
	if(window.XMLHttpRequest) // FIREFOX
		xhr_object = new XMLHttpRequest();
	else if(window.ActiveXObject) // IE
		xhr_object = new ActiveXObject('Microsoft.XMLHTTP');
	else
		return(false);
	xhr_object.open('GET', fichier, false);
	xhr_object.send(null);
	if(xhr_object.readyState == 4) return(xhr_object.responseText);
	else return(false);
}

function getURLParameter(name) {
    return decodeURI(
        (RegExp(name + '=' + '(.+?)(&|$)').exec(location.search)||[,null])[1]
    );
}

function removeURLParameter(url, name){
    value = getURLParameter(name);
    if(url.indexOf("&amp;" + name + "=") != -1) url = url.replace("&amp;" + name + "=" + value, "");
    else if(url.indexOf("&" + name + "=") != -1) url = url.replace("&" + name + "=" + value, "");
    else url = url.replace(name+"=" + value, "");
    return url;
}

function getElementsByClassName(node,classname) {
	  if (node.getElementsByClassName) { // use native implementation if available
	    return node.getElementsByClassName(classname);
	  } else {
	    return (function getElementsByClass(searchClass,node) {
	        if ( node == null )
	          node = document;
	        var classElements = [],
	            els = node.getElementsByTagName("*"),
	            elsLen = els.length,
	            pattern = new RegExp("(^|\\s)"+searchClass+"(\\s|$)"), i, j;

	        for (i = 0, j = 0; i < elsLen; i++) {
	          if ( pattern.test(els[i].className) ) {
	              classElements[j] = els[i];
	              j++;
	          }
	        }
	        return classElements;
	    })(classname, node);
	  }
	}

function rgbToHex(color){
    if(color.substr(1) == "#")
        return color.toLowerCase();
    if(color.toLowerCase().indexOf("rgb") == -1)
        return color.toLowerCase();

    var digits = /(.*?)rgb\(\s*(\d+), \s*(\d+), \s*(\d+)\)/.exec(color);

    var red = parseInt(digits[2]);
    var green = parseInt(digits[3]);
    var blue = parseInt(digits[4]);

    var rgb = blue | (green << 8) | (red << 16);
    return "#" + rgb.toString(16).toLowerCase();
}

function showgenesearch(){
    document.getElementById("gene_box").style.display = "block";
    box = document.getElementById("blast_box");
    box.style.display = "none";
}

function showblastsearch(){     
    document.getElementById("blastdb").innerHTML = file('blastdb.pl');
    document.getElementById('blast_box').style.display = 'block';
    document.getElementById("gene_box").style.display = "none";
}


function verifySequence(){
    var query = document.getElementById("blastquery").value;
    var goblast = document.getElementById("submitblast");
    //check empty sequence
    if(query == ""){
        blastWarning('empty');   
    }
   // check fasta format
    else if(query.indexOf(">") > -1){
        var count = query.match(/>/g);
        if(count.length > 1){
            //check if first sequence is good
            var firstSeq = (query.split(">"))[1];
            if((new RegExp(/[^A-Za-z\n\s\t]/)).test((firstSeq.split("\n"))[1]))
                blastWarning('wrongformat');
            else blastWarning('onesequence');
        }
        else{
            sequence = query.split("\n");
            if((new RegExp(/[^A-Za-z\n\s\t]/)).test(sequence[1])){
                blastWarning('wrongformat');
            }
            else{
                if(verifyCheckbox()){ goblast.submit(); }
                else{ blastWarning('nodb'); }
            }
        }
    }
    else{
        if((new RegExp(/[^A-Za-z\n\s\t]/)).test(query)){
            blastWarning('wrongformat');
        }
        else{
            if(verifyCheckbox())
                goblast.submit();
            else blastWarning('nodb');
        }
    }
}

function verifyCheckbox(){
    var checkboxes = document.getElementsByName("blastdb");
    for(var i = 0; i < checkboxes.length; i++){
        if(checkboxes[i].checked)
            return true;
    }
    return false;
}

var confirmBox = function(_id){
    this.id = _id;
    this.title = '';
    this.text = '';
    this.options = new Array();
    
    this.addOption = function(txt, val){
        var o = [txt,val]
            this.options.push(o);
    }

    this.setContent = function(title, body){
        var link = "";
        var txt = "";
        var val = "";
        
        document.getElementById('head').innerHTML = this.title;
        document.getElementById('pconf').innerHTML = this.body;
        document.getElementById('spanconf').innerHTML = '';
        
        for(var i=0; i< this.options.length; i++){
            txt = this.options[i][0];
            val = this.options[i][1];
            link = '<input type="button" class="btn btn-small" name="blast" value="' + txt + '" onclick="'+ val +'"/>';
            document.getElementById('spanconf').innerHTML += link + ' ';
        } 
    }

    this.open = function(){
        this.setContent();
        if(this.visible){
            $('#genoConfirm').attr('style','border:none;display:none');
        }
        else{
            $('#leftpanel').attr('style', 'opacity:0.2');
            $('#rightpanel').attr('style', 'opacity:0.2');
            $('#oneseq').attr('style','display:block; opacity:1'); 
            $('input[name=blast]').each(function(){ this.focus(); });
            $('#goblast').disabled = true;
        }   
    }
}

function confirmBtn(txt,message){
    var box = document.getElementById('oneseq');
    box.style.display = 'none';
    box.style.border = 'none';
            
    $('#leftpanel').attr('style','opacity:1');
    $('#rightpanel').attr('style','opacity:1');
    if(message == 'onesequence'){
        if(txt == "yes"){
            document.getElementById('submitblast').submit();
        }
        else { 
            document.getElementById('blastquery').focus(); 
        }
    }
    else if(message == 'wrongformat'){
        document.getElementById('blastquery').focus();
        return;
    }
}


function blastWarning(message){
    var genoConfirm = new confirmBox('oneseq');
    genoConfirm.title = 'Warning';
    if(message == 'onesequence'){
        genoConfirm.body = 'You have entered more than 1 sequence.<br/> We will only process your first sequence.<br/>Do you want to continue?';
        genoConfirm.addOption("Yes", "confirmBtn('yes','onesequence')");
        genoConfirm.addOption("No", "confirmBtn('no','onesequence')");
    }
    else if(message == 'wrongformat'){
        genoConfirm.body = 'Your sequence contains invalid characters';
        genoConfirm.addOption("Close","confirmBtn('close','wrongformat')");
    }
    else if(message == 'empty'){
        genoConfirm.body = 'Please enter your sequence';
        genoConfirm.addOption("Close", "confirmBtn('close','wrongformat')");
    }
    else if(message == 'nodb'){
        genoConfirm.body = 'Please choose the database(s)';
        genoConfirm.addOption("Close", "confirmBtn('close','wrongformat')");
    }
    genoConfirm.open();
}

function blastOptionsInfo(){
    $('#leftpanel').attr('style','opacity:0.2');
    $('#rightpanel').attr('style','opacity:0.2');
    $('#blastOptInfo').attr('style','display:inline;top:10%;display:inline;opacity:1');
}
function closeInfo(){
    $('#blastOptInfo').attr('style','display:none');
    $('#leftpanel').attr('style','opacity:1');
    $('#rightpanel').attr('style','opacity:1');
}

function confirmOpt(e){
    if(e.which == 13){
        verifySequence();
        ev = e ? e : window.event;
        ev.preventDefault();
    }
}

function genedetail(ev, cmd){
    e = ev ? ev : window.event;
    el = document.getElementById("infocontent");
    contextisvisible = 1;
    el.style.left = pageXOffset + e.clientX + 5 + 'px';
    el.style.top = pageYOffset + e.clientY + 10 + 'px';
    el.innerHTML = retrInfo(cmd);
    el.style.visibility = 'visible';
}


$(document).scroll(function(e){
	if($('#refreshSpec').css('display') == 'none'){	
	    $('#leftpanelphylohide').css({
                'left': 70 - $(document).scrollLeft()});
        }
        else{ 
            $('#leftpanelphylohide').css({'left': 395 - $(document).scrollLeft() });
        }
});