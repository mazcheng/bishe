<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <link type="text/css" rel="stylesheet" href="../tpl/css/style.css">
<style>
body{
	background-image: none;body{background-color:#fff; font-size:12px;}
}
</style>

<script language="JavaScript" type="text/javascript"> 
	function find(s1, s2)
	{
		var str1 = s1;
		var str2 = s2;
		var len1 = str1.length;
		var len2 = str2.length;
		var i;
		if (len1 < len2)
			return 0;
		else
		{
			for (var i=0;i<len2;i++)
			{
				if (str1.charAt(i) != str2.charAt(i))
				{
					return 0;
				}
			}
		} 
		return 1;
	}
	function test(obj)
	{  
		var objname = obj.id;
		var name;  
		var s = ""; 
		var imgnode =  document.getElementById("img_" + objname);
		var showvalue = ""; 
		if (imgnode.alt == "展开")
		{ 
			imgnode.src = "../tpl/images/close.png";
			imgnode.alt = "缩回";
			showvalue="block";
		}
		else
		{
			imgnode.src = "../tpl/images/open.png";
			imgnode.alt = "展开";
			showvalue="none"; 
		}
		for (var i=0; i<document.all.length; i++)
		{
			name = document.all.item(i).id; 
			if (!((name == "")||(name == null)||(name == objname)))
			{    
				s = name;
				if (find(s,objname))
				{  
					document.all.item(i).style.display = showvalue;
				}
			}
		}    
	}
</script>

<style type="text/css">
	.stepright1{padding-left:5px;}
	.stepright2{padding-left:15px;}
	.stepright3{padding-left:25px;}
	.stepright4{padding-left:35px;}
	.stepright5{padding-left:45px;}
	.stepright6{padding-left:55px;}
	.stepright7{padding-left:65px;}
	div.Leaf { font: bold;}
	body{ background-color:#FFFFFF;}
</style>


</head><body><div style="text-align:left;">
<div class="left_content">
                <p><select style="width:98%;" class="option" name="s_doctype" size="1" id="s_doctype" onchange="changeClick()">
                    <option value="all">所有文献类型</option>
                    <option value="00">规范文档</option><option value="01">中文图书</option><option value="02">西文图书</option><option value="03">日文图书</option><option value="04">俄文图书</option><option value="05">中文光盘</option><option value="06">外文光盘</option><option value="11">中文期刊</option><option value="12">西文期刊</option><option value="13">日文期刊</option><option value="14">俄文期刊</option><option value="29">电子图书</option><option value="30">电子期刊</option><option value="31">中文古籍</option><option value="32">非中文古籍</option><option value="33">乐谱手稿</option><option value="34">印刷乐谱</option><option value="35">计算机文档</option><option value="36">测绘资料</option><option value="37">非音乐录音</option><option value="38">音乐录音</option><option value="39">录像资料</option><option value="40">电影胶片</option><option value="41">投影幻灯</option><option value="42">缩微制品</option><option value="43">手稿</option><option value="44">书法绘画</option><option value="45">金石拓片</option><option value="46">三维制品</option><option value="47">混合型资料</option><option value="99">类型不详</option>                  </select></p>
                  <p class="Opened" style="padding:5px;"><a href="cls_browsing_tree.php"><strong>中图法</strong></a>
      </p><div style="display: block;" class="stepright1" id="nodeA" name="nodeA" onclick="test(this)"><a href="javascript:expandTree('A',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeA" name="img_nodeA" alt="展开"></a>A 马列主义、毛泽东思想、邓小平理论</div> <div style="display: block;" class="stepright1" id="nodeB" name="nodeB" onclick="test(this)"><a href="javascript:expandTree('B',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeB" name="img_nodeB"></a>B 哲学、宗教</div> <div style="display: block;" class="stepright1" id="nodeC" name="nodeC" onclick="test(this)"><a href="javascript:expandTree('C',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeC" name="img_nodeC"></a>C 社会科学总论</div> <div style="display: block;" class="stepright1" id="nodeD" name="nodeD" onclick="test(this)"><a href="javascript:expandTree('D',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeD" name="img_nodeD"></a>D 政治、法律</div> <div style="display: block;" class="stepright1" id="nodeE" name="nodeE" onclick="test(this)"><a href="javascript:expandTree('E',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeE" name="img_nodeE"></a>E 军事</div> <div style="display: block;" class="stepright1" id="nodeF" name="nodeF" onclick="test(this)"><a href="javascript:expandTree('F',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeF" name="img_nodeF"></a>F 经济</div> <div style="display: block;" class="stepright1" id="nodeG" name="nodeG" onclick="test(this)"><a href="javascript:expandTree('G',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeG" name="img_nodeG"></a>G 文化、科学、教育、体育</div> <div style="display: block;" class="stepright1" id="nodeH" name="nodeH" onclick="test(this)"><a href="javascript:expandTree('H',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeH" name="img_nodeH"></a>H 语言、文字</div> <div style="display: block;" class="stepright1" id="nodeI" name="nodeI" onclick="test(this)"><a href="javascript:expandTree('I',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeI" name="img_nodeI"></a>I 文学</div> <div style="display: block;" class="stepright1" id="nodeJ" name="nodeJ" onclick="test(this)"><a href="javascript:expandTree('J',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeJ" name="img_nodeJ"></a>J 艺术</div> <div style="display: block;" class="stepright1" id="nodeK" name="nodeK" onclick="test(this)"><a href="javascript:expandTree('K',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeK" name="img_nodeK"></a>K 历史、地理</div> <div style="display: block;" class="stepright1" id="nodeN" name="nodeN" onclick="test(this)"><a href="javascript:expandTree('N',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeN" name="img_nodeN"></a>N 自然科学总论</div> <div style="display: block;" class="stepright1" id="nodeO" name="nodeO" onclick="test(this)"><a href="javascript:expandTree('O',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeO" name="img_nodeO"></a>O 数理科学与化学</div> <div style="display: block;" class="stepright1" id="nodeP" name="nodeP" onclick="test(this)"><a href="javascript:expandTree('P',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeP" name="img_nodeP"></a>P 天文学、地球科学</div> <div style="display: block;" class="stepright1" id="nodeQ" name="nodeQ" onclick="test(this)"><a href="javascript:expandTree('Q',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeQ" name="img_nodeQ"></a>Q 生物科学</div> <div style="display: block;" class="stepright1" id="nodeR" name="nodeR" onclick="test(this)"><a href="javascript:expandTree('R',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeR" name="img_nodeR"></a>R 医药、卫生</div> <div style="display: block;" class="stepright1" id="nodeS" name="nodeS" onclick="test(this)"><a href="javascript:expandTree('S',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeS" name="img_nodeS"></a>S 农业科学</div> <div style="display: block;" class="stepright1" id="nodeT" name="nodeT" onclick="test(this)"><a href="javascript:expandTree('T',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeT" name="img_nodeT"></a>T 工业技术</div> <div style="display: block;" class="stepright1" id="nodeU" name="nodeU" onclick="test(this)"><a href="javascript:expandTree('U',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeU" name="img_nodeU"></a>U 交通运输</div> <div style="display: block;" class="stepright1" id="nodeV" name="nodeV" onclick="test(this)"><a href="javascript:expandTree('V',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeV" name="img_nodeV"></a>V 航空、航天</div> <div style="display: block;" class="stepright1" id="nodeX" name="nodeX" onclick="test(this)"><a href="javascript:expandTree('X',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeX" name="img_nodeX"></a>X 环境科学,安全科学</div> <div style="display: block;" class="stepright1" id="nodeZ" name="nodeZ" onclick="test(this)"><a href="javascript:expandTree('Z',1)"><img border="0" src="../tpl/images/open.png" title="展开" id="img_nodeZ" name="img_nodeZ"></a>Z 综合性图书</div> <p></p>
</div>
</div>

<script type="text/javascript">

var clsNo;
var cslNameCurrent;

function expandTree(cls,lvl)
{
    var url = "cls_browsing_tree.php?s_doctype=" + document.getElementById('s_doctype').value + "&cls=" + cls + "&lvl=" + lvl+ "#node" + cls;
	top.window.tree.location.href= url;
}

function searchF(cls,clsName)
{
    clsNo = cls;
    clsNameCurrent = clsName;
    
	var url = "cls_browsing_book.php?s_doctype=" + document.getElementById('s_doctype').value + "&cls=" + cls + "&clsname=" + clsName ;
	top.window.main.location.href = url;
}

function changeClick()
{
    if(clsNo && clsNameCurrent)
    {
        var url = "cls_browsing_book.php?s_doctype=" + document.getElementById('s_doctype').value+ "&cls=" + clsNo + "&clsname=" + clsNameCurrent;
    	top.window.main.location.href = url;
    }
}
</script>
</body></html>