DATA = """














<html>





























































<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">










	<script language="javascript" type="text/JavaScript" src="https://esaj.tjms.jus.br/sajcas/verificarLogin.js?script=1558602733027"></script>

	<script language="javascript">
		if(window.sajcas && window.sajcas.usuarioLogadoNoCasServer) {
			var urlRetornoSistema = '';
			if(urlRetornoSistema === '') {
				urlRetornoSistema = window.location.href;
			}

			if(urlRetornoSistema.lastIndexOf('?') != -1) {
				urlRetornoSistema += '&';
			} else {
				urlRetornoSistema += '?';
			}
			urlRetornoSistema+= 'gateway=true';
			window.location.href = urlRetornoSistema;
		}
	</script>


	<title>Portal de Serviços e-SAJ</title>
































<!-- Includes do spw -->

<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(3),u=e(4),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[c.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf("Chrome")===-1&&u.indexOf("Chromium")===-1&&(o="Safari",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+x.offset],null,"api");var t=l.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===l.readyState&&i()}function i(){f("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e("handle"),c=e(3),s=e("ee"),p=e(2),d=window,l=d.document,m="addEventListener",v="attachEvent",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1123.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m]("DOMContentLoaded",i,!1),d[m]("load",r,!1)):(l[v]("onreadystatechange",o),d[v]("onload",r)),f("mark",["firstbyte",u],null,"api");var E=0,O=e(5)},{}]},{},["loader"]);</script><link rel="stylesheet" href="/cpopg5/css/spw/spwConcatenado.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg5/css/esaj.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg5/css/saj/saj-captcha.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg5/css/cpo.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg5/css/formulario.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg5/css/saj/saj-popup-modal.css" type="text/css"/>

<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />

<script language="javascript" type="text/JavaScript" src="/cpopg5/js/jquery/jquery.min.js?n=f85078e0-6721-4b8e-a0a6-dfbf8be86d25"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/jquery/jquery.func_toggle.js?n=cfefeab3-4504-41e5-afaa-8a71b72ba76c"></script>
<script language="javascript" type="text/javascript" src="/cpopg5/js/jquery/jquery.jplayer.2.9.2.min.js?n=8b2ef003-d258-4853-afa6-99c119ce780e"></script>
<script language="javascript" type="text/javascript" src="/cpopg5/js/jquery/jquery.blockUI.min.js?n=87d970bd-a258-4880-a0d9-8848d69fdb8e"></script>
<script language="javascript" type="text/javascript" src="/cpopg5/js/jquery/jquery.browser.min.js?n=57ff66c6-3e5c-4c3f-af85-80d6e36b7841"></script>

<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-web-2.2.41-4.js?n=30970c6c-43a1-4aff-b78f-8e9725b9408e"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-tooltip.js?n=54c7d58f-c24f-435c-9d1d-9c01195d2c01"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-popup-modal-1.0.0-1.js?n=2cf0ab0e-4af5-4879-b5e9-e641eb85c552"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-browser.js?n=b6fb5947-4eaf-412d-b4af-c1aedcf6b900"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-mascara-input.js?n=b2a79016-bb42-4f69-a256-66fdeb761bfa"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/saj-numeroProcesso.js?n=7d2a8037-12b2-416e-a9b8-a0d347b507b6"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/spw/spwConcatenado.js?n=3e07d40e-acf4-433d-916d-f01206cdc3e3"></script>


<script>
	window.saj = window.saj || {};
	window.saj.env = window.saj.env || {};
	window.saj.env.root = '/cpopg5';
	window.saj.env.css = '/cpopg5/css';
	window.saj.env.js = '/cpopg5/js';
	window.saj.env.imagens = '/cpopg5/imagens';
	window.saj.env.queryString = 'processo.codigo=01001ZB2W0000&processo.foro=1&uuidCaptcha=sajcaptcha_b0faa30af0f4404b811a76c421826bdd';

	window.saj.cpo = window.saj.cpo || {};

	// transfere variavel se cpo esta rodando para totem
	window.saj.cpo.totem = 'false' == 'true';
</script>

<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj-cpo-cbpesquisa.js?n=629714429"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/formulario.js?n=1425064359"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg5/js/saj/acessibilidade/acessibilidade.js?n=097794ef-89eb-46b4-8b4b-2c47ffda2ec7"></script>





<script>
	(function($){
		$(function(){
			var intervalo = 1795000;
			$.saj.manterSessao('/cpopg5/manterSessao.do', intervalo);
		});

	})(jQuery);
</script>





    <script language="javascript" type="text/JavaScript">
        $.saj = $.saj || {};
        $.saj.acessoRecurso = {
            abrirPastaDigitalEmPopup: 'true' == 'true',
            idRecursoQueProvocouLiberacaoPorSenha: '',
            popupSenha: {
                mostrar: 'false' == 'true',
                titulo: 'Digite a senha do processo',
                altura: 220 + Number("10"),
                alturaAdicionalParaMensagemValidacao: Number("0"),
                largura: 480
            }
        };

        $.saj.getUrlParameter = function getUrlParameter(sParam) {
            var sPageURL = decodeURIComponent(window.location.search.substring(1)), sURLVariables = sPageURL.split('&'), sParameterName, i;
            for (i = 0; i < sURLVariables.length; i++) {
                sParameterName = sURLVariables[i].split('=');
                if (sParameterName[0] === sParam) {
                    return sParameterName[1] === undefined ? true : sParameterName[1];
                }
            }
        };
    </script>
    <script language="javascript" type="text/JavaScript" src="/cpopg5/jsp/show-2.8.33-0.js?n=2077829452"></script>






















<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<meta http-equiv="pragma" content="no-cache"/>
<meta http-equiv="cache-control" content="no-cache"/>
<meta http-equiv="expires" content="0"/>

<link href="https://esaj.tjms.jus.br/esaj/tema/padrao/css/esajComum.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjms.jus.br/esaj/tema/padrao/css/esajLayout.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjms.jus.br/esaj/tema/padrao/clientes/MS/css/esajLayoutMS.css" rel="stylesheet" type="text/css" />

<style type="text/css">
<!--
/* botao default means o mais claro, que seria o "botï¿½o principal" */
.spwBotaoDefault, .spwBotaoDefault-o {
	background-image: url(https://esaj.tjms.jus.br/esaj/tema/padrao/clientes/MS/imagens/layout/fundoBotaoDefault.gif);
}
/* o botao secundario, menos provavel de ser clicado, mais escuro */
.spwBotao, .spwBotao-o {
	background-image: url(https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/fundoBotao.gif);
}
-->
</style>


<script language="javascript" type="text/JavaScript" src="https://esaj.tjms.jus.br/esaj/tema/padrao/js/menu.js?n=2553626853"></script>

<link rel="shortcut icon" href="https://esaj.tjms.jus.br/esaj/tema/padrao/clientes/MS/imagens/favicon.ico" type="image/x-icon" />







	<script type="text/javascript">
		(function($) {
			$(function(){
				// Correção temporária do alinhamento do divisor de seção de formulário do SPW
				$('td[background$="spw/fundo_subtitulo2.gif"]').attr('valign', 'top');

			})
		})(jQuery);
	</script>
</head>


<body>
<div class="div-conteudo">







































































		<table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaCabecalhoCliente" summary=" ">
	<tr>
		<td><a href="http://www.tjms.jus.br"><img src="https://esaj.tjms.jus.br/esaj/tema/padrao/clientes/MS/imagens/layout/cabecalhoLogo.jpg" width="241" height="57" alt="Tribunal de Justiça de MS" /></a></td>
	</tr>
</table>





















<!-- cabecalho e-Saj -->
<table width="100%" cellpadding="0" cellspacing="0" class="esajTabelaCabecalhoServico" summary=" ">
	<tr>
		<td class="esajCelulaCabecalhoServicoLogo">




<a href="https://esaj.tjms.jus.br/esaj/redirecionarNovoEsaj.do"><img src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/eSajServico.gif" title="Voltar para página inicial do e-SAJ" alt="Voltar para página inicial do e-SAJ" width="255" height="53" border="0" /></a><img src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/eSajServicoInf.gif" alt=" " width="255" height="28" border="0" /></td>
		<td class="esajCelulaCabecalhoServicoMenu">
		    <table width="100%" border="0" cellpadding="0" cellspacing="0" summary=" ">
				<tr>
					<td align="right">











        <div id="divopupContato" style="display: none;">
                <br>
<b>Suporte Técnico de Sistemas</b>
<p>Central de serviços de TI<p/>
(67) 3314-1718
</p>
Horários de atendimento: </br>
De Segunda à Sexta-feira das 07h às 20h </br>
<i>*exceto feriados Federais e Estaduais</i>
        </div>


<!-- Devido ao alinhamento inline das imagens, elas não podem ter nenhum tipo de espaçamento entre elas, portanto é necessário finalizar a linha iniciando um comentário e fechar o comentário imediatamente antes da abertura da nova tag-->
<img height="24" width="47" alt=" " src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/inicioMenuSup.jpg"/><a href="https://esaj.tjms.jus.br/caixapostal"><!--
--><img height="24" width="83" border="0" alt="Caixa postal" src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/caixaPostal.gif"/></a><!--
--><img height="24" width="4" alt=" " src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a href="https://esaj.tjms.jus.br/esaj/cadastro.do"><!--
--><img src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/cadastro.gif" alt="Cadastro" width="81" height="24" border="0" /></a><!--

    --><img height="24" width="4" alt=" " src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a id="linkContato" href="#"><!--
    --><img height="24" width="68" border="0" alt="Contato" src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/contato.gif"/></a><!--


    --><img height="24" width="4" alt=" " src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a target="blank" href="https://esaj.tjms.jus.br/WebHelp/"><!--
    --><img height="24" width="61" border="0" alt="Ajuda do e-Saj" src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/ajuda.gif"/></a><!--


--></td>
				</tr>
				<tr>
					<td class="esajCelulaIdentificacaoServico" >




<style>

    td.esajCelulaIdentificacao, td.esajCelulaIdentificacaoServico {
        position: relative;
    }

    button.escolhaBeta {
        border: 0;
        background: #0078D7;
        color: #fff;
        margin-right: 5px;
        font-family: verdana;
        font-size: 12px;
        height: 27px;
        line-height: 14px;
        border-radius: 0;
        text-shadow: 1px 1px 1px #797979;
        position: absolute;
        top: 30px;
        right: 3px;
        padding: 7px 12px;
        cursor: pointer;
    }

    button.escolhaBeta:hover {
        background-color: #0b5c9c;
    }
</style>

<span id="identificacao"></span>

<button style="display: none" class="escolhaBeta"></button>






        <script language="javascript" type="text/JavaScript" src="https://esaj.tjms.jus.br/sajcas/conteudoIdentificacao?script=1558125792046"></script>


</td>
				</tr>
				<tr>
					<td class="esajCelulaCabecalhoServicoCaminho" >












































<a href="" class="esajCaminhoLink"></a>

 &gt;


<a href="https://esaj.tjms.jus.br/esaj/portal.do?servico=740000" class="esajCaminhoLink">Bem-vindo</a>

 &gt;


<a href="https://esaj.tjms.jus.br/esaj/portal.do?servico=190090" class="esajCaminhoLink">Consultas</a>

 &gt;



Consulta de Processos de 1º Grau
</td>
				</tr>
			</table>
		</td>
	</tr>
</table>
<!-- CONTEUDO -->
<table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaTitulo">
	<tr>
		<td class="esajCelulaMenuSuspenso">
		<a href="#" onclick="return showMenuSuspenso()"><img src="https://esaj.tjms.jus.br/esaj/tema/padrao/imagens/layout/menuSuspenso.gif" alt="Menu de servi&ccedil;os" width="243" height="21" style="display:block" /></a>
		<div id="layerMenu" style="display:none">


<!-- MENU -->
<ul id="esajMenuArea">
	<li class="esajMenuAberto"><a href="#" onclick="return esajMenu(this)">Consultas</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cpopg5/open.do">Processos de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cposg5/open.do">Processos de 2º Grau</a></li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Ordem de Processos</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do">Julgamento de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do">Publicação e Cumprimento de Atos de 1º Grau</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pauta-julgamento/consulta">Pauta de Julgamento</a></li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Jurisprudência</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cjsg/consultaSimples.do">Simples</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cjsg/consultaCompleta.do">Completa</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/cdje">Diário da Justiça Eletrônico</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Recolhimento de Custas</a>
<ul>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Custas de 1º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=6&flTipoCusta=0&cdServicoCalculoCusta=690003">Emitir Custas</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=9&flTipoCusta=1&cdServicoCalculoCusta=690005">Diligências de Oficial de Justiça</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=11&flTipoCusta=5&cdServicoCalculoCusta=690004">Serviços</a></li>
  <li class="esajMenuItem"><a href="https://www.tjms.jus.br/legislacao/visualizar.php?lei=32463">Consulta à tabela de valor das diligências</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/abrirConsultaCustas.do">Consulta de Custas</a></li>
  <li class="esajMenuItem"><a href="http://www.sefaz.ms.gov.br/uferms/">Link para consultar o valor da UFERMS</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Custas de 2º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdTipoCusta=23&flTipoCusta=6&cdServicoCalculoCusta=690202">Emitir Preparo de Recursos</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdTipoCusta=9&flTipoCusta=1&cdServicoCalculoCusta=690209">Diligências de Oficial de Justiça</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdTipoCusta=6&flTipoCusta=0&cdServicoCalculoCusta=690015">Emitir Custas Iniciais</a></li>
  <li class="esajMenuItem"><a href="https://www.tjms.jus.br/legislacao/visualizar.php?lei=32463">Consulta à tabela de valor das diligências</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/abrirConsultaCustasSg.do">Consulta de Custas</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdTipoCusta=11&flTipoCusta=5&cdServicoCalculoCusta=690203">Serviços</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Custas dos Juizados</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=17&flTipoCusta=1&cdServicoCalculoCusta=690011">Emitir custas / Preparo</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=28&flTipoCusta=1&cdServicoCalculoCusta=690012">Link para recolhimento do FUNADEP - Fora de uso</a></li>
  <li class="esajMenuItem"><a href="http://www.sefaz.ms.gov.br/uferms/">Link para consultar o valor da UFERMS</a></li>
</ul>
  </li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petpg/abrirVerificacaoRequisitosPet.do">Verificação de Requisitos</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petpg/abrirNovaPeticaoInicial.do">Peticionamento Inicial de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petpg/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petpg/abrirConsultaPeticoes.do">Consulta de Petições de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pettr/abrirNovaPeticaoInicial.do">Peticionamento Inicial nas Turmas Recursais</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pettr/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário nas Turmas Recursais</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pettr/abrirConsultaPeticoes.do">Consulta de Petições nas Turmas Recursais</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petsg/abrirNovaPeticaoInicial.do">Peticionamento Inicial de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petsg/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/petsg/abrirConsultaPeticoes.do">Consulta de Petições de 2º Grau</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Push - Acompanhar Processo Judicial</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/push">1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pushsg5tr">2º Grau</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Intimação e Citação Eletrônica</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/intimacoesweb/abrirConsultaAtosNaoRecebidos.do">Recebimento</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/intimacoesweb/abrirConsultaAtosRecebidos.do">Consulta das Recebidas</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/sco/abrirCadastro.do">Pedido de Certidão de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/scosg/abrirCadastro.do">Pedido de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/sco/abrirConferencia.do">Conferência de Certidão de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/scosg/abrirConferencia.do">Conferência de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/sco/abrirDownload.do">Baixar Certidão de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/scosg/abrirDownload.do">Baixar Certidão de 2º Grau</a></li>
</ul>
  </li>
	<li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Conferência de Documentos</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pastadigital/pg/abrirConferenciaDocumento.do">Documento Digital de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjms.jus.br/pastadigital/sgcr/abrirConferenciaDocumento.do">Documento Digital de 2º Grau</a></li>
</ul>
  </li>
</ul>

		</div>
		</td>
		<td class="esajCelulaTituloServico"><h1 class="esajTituloPagina">Consulta de Processos de 1º Grau</h1></td>
	</tr>
</table>
<table width="100%" cellpadding="0" cellspacing="0" summary=" ">
	<tr>
		<td class="esajCelulaConteudoServico" >



















































    <span class="esajTituloOrientacoes">Orientações</span>




            <ul class="esajUlOrientacoes" id="">


















	<li>
























Processos distribuídos no mesmo dia podem ser localizados se buscados pelo número do processo, com o seu foro selecionado.



	</li>
























































	<li>
























Dúvidas? Clique <a style="cursor:pointer" class="layout" onclick="popup('/WebHelp/id_consultas_processuais.htm','','location=no, toolbar=no, resizable=yes, width=795, height=560, scrollbars=yes')">aqui</a> para mais informações sobre como pesquisar.



	</li>




















	<li>
























Processos baixados, em segredo de justiça ou distribuídos no mesmo dia serão apresentados somente na pesquisa pelo número do processo.



	</li>




            </ul>




    <br>


















<form name="consultarProcessoForm" method="GET" action="/cpopg5/search.do" autocomplete="off" enctype="" onsubmit="return applySubmit(this, eval('function spwSubmit(t, e){decodificaInputMulSelOnSubmit();if (!IS_enableSubmit) return false; return BENV_isCamposValidos(t); } spwSubmit(this, event);'));" id="formConsulta" target="">
	<input type="hidden" name="conversationId" value="">








































	<div class="">

			<br/>














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">



					<h2 class="subtitle">
						Dados para pesquisa

					</h2>


		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



			<br/>

		<table id="secaoFormConsulta" class="secaoFormBody" width="100%" style="" cellpadding="2" cellspacing="0" border="0">




















































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="id_Comarca" class="" style="text-align:right;font-weight:bold;;">Comarca:</label>


		  </td>





		    <td valign="">











		<select name="dadosConsulta.localPesquisa.cdLocal" id="id_Comarca" obrigatorio="" rotulo="Comarca"><option value="-1">

























Todas comarcas

</option>

			<option value="111">1ª Vara Juizado Especial de Campo Grande</option>
<option value="104">4ª Vara Juizado Especial de Campo Grande</option>
<option value="105">5ª Vara Juizado Especial de Campo Grande</option>
<option value="115">7ª Vara Juizado Especial de Campo Grande</option>
<option value="108">8ª Vara Juizado Especial de Campo Grande</option>
<option value="109">9ª Vara Juizado Especial de Campo Grande</option>
<option value="49">Agua Clara</option>
<option value="4">Amambai</option>
<option value="52">Anastácio</option>
<option value="22">Anaurilândia</option>
<option value="23">Angélica</option>
<option value="24">Aparecida do Taboado</option>
<option value="5">Aquidauana</option>
<option value="25">Bandeirantes</option>
<option value="26">Bataguassu</option>
<option value="27">Batayporã</option>
<option value="3">Bela Vista</option>
<option value="28">Bonito</option>
<option value="30">Brasilândia</option>
<option value="31">Caarapó</option>
<option value="6">Camapuã</option>
<option value="1" selected="selected">Campo Grande</option>
<option value="7">Cassilândia</option>
<option value="62">CEJUSC - JUIZADOS</option>
<option value="57">CEJUSCs</option>
<option value="46">Chapadão do Sul</option>
<option value="58">Coronel Sapucaia</option>
<option value="8">Corumbá</option>
<option value="9">Costa Rica</option>
<option value="11">Coxim</option>
<option value="32">Deodápolis</option>
<option value="53">Dois Irmãos do Buriti</option>
<option value="2">Dourados</option>
<option value="33">Eldorado</option>
<option value="10">Fátima do Sul</option>
<option value="34">Glória de Dourados</option>
<option value="35">Iguatemi</option>
<option value="36">Inocência</option>
<option value="37">Itaporã</option>
<option value="51">Itaquiraí</option>
<option value="12">Ivinhema</option>
<option value="13">Jardim</option>
<option value="110">Juizado Especial Central de Campo Grande</option>
<option value="101">Juizado Especial de Dourados</option>
<option value="114">Juizado Especial de Três Lagoas</option>
<option value="600">Justiça Itinerante do Estado de MS</option>
<option value="14">Maracaju</option>
<option value="15">Miranda</option>
<option value="16">Mundo Novo</option>
<option value="29">Naviraí</option>
<option value="38">Nioaque</option>
<option value="54">Nova Alvorada do Sul</option>
<option value="17">Nova Andradina</option>
<option value="18">Paranaíba</option>
<option value="39">Pedro Gomes</option>
<option value="800">Plantão</option>
<option value="19">Ponta Porã</option>
<option value="40">Porto Murtinho</option>
<option value="41">Ribas do Rio Pardo</option>
<option value="20">Rio Brilhante</option>
<option value="48">Rio Negro</option>
<option value="42">Rio Verde de Mato Grosso</option>
<option value="43">São Gabriel do Oeste</option>
<option value="44">Sete Quedas</option>
<option value="45">Sidrolândia</option>
<option value="55">Sonora</option>
<option value="47">Terenos</option>
<option value="21">Três Lagoas</option>
<option value="102">Unid. 102 Juizado Especial - Dourados</option>
<option value="103">Unid. 103 Juizado Esp. - Mata do Jacinto</option>
<option value="106">Unid. 106 Juizado Esp. - MicroEmpresas</option>
<option value="107">Unid. 107 Juizado Esp. - Consumidor</option>
<option value="112">Unid. 112 Juizado Esp. Central Criminal</option>
<option value="998">Unidade de Teste 2 - DAJ</option>
<option value="999">Unidade de Teste DAJ - USO EXCLUSIVO TJ</option></select>







		</td>

			</tr>





































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="cbPesquisa" class="" style="text-align:right;font-weight:bold;;">Pesquisar por:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>













<select name="cbPesquisa" id="cbPesquisa"><option value="NUMPROC" selected="selected">Número do Processo</option>

 		<option value="NMPARTE">Nome da parte</option>

 		<option value="DOCPARTE">Documento da Parte</option>

 		<option value="NMADVOGADO">Nome do Advogado</option>

 		<option value="NUMOAB">OAB</option>

 		<option value="PRECATORIA">Nº da Carta Precatória na Origem</option>

 		<option value="DOCDELEG">Nº do Documento na Delegacia</option></select>



			</td>
		</tr>
	  </table>







		</td>

			</tr>





































































		<script>$.saj.numeroProcesso.desabilitarNumeroOculto = false;</script>




























<script type="text/javascript">
	(function($){
		$(function() {
			if($.browser.msie){
				$('.grupoRadio').find('input:radio:visible:enabled').attr('aria-required','');
				return;
			}
			$('.grupoRadio').attr('aria-required','').attr('required','');
		});
	})(jQuery);
</script>










































				<tr class="">





		  <td id="" width="150" valign="">

		  </td>





		    <td valign="">








	<table cellspacing="0" border="0" width="">
		<tr>
			<td>

				<fieldset class="grupoRadio" style="margin:0;padding:0;border:none" >
					<legend style="display:block;font-size:0;">
						Tipo do número
					</legend>

			   <input type="radio" name="dadosConsulta.tipoNuProcesso" value="UNIFICADO" checked="checked" id="radioNumeroUnificado"><label for="radioNumeroUnificado">Unificado</label>
			   <input type="radio" name="dadosConsulta.tipoNuProcesso" value="SAJ" id="radioNumeroAntigo"><label for="radioNumeroAntigo">Outros</label>

				</fieldset>

			</td>
		</tr>
	  </table>







		</td>

			</tr>



































































				<tr id="NUMPROC" class="">




		  <td id="" width="150" valign="">





		  	    <label for="" class="" style="text-align:right;font-weight:bold;;">Número do Processo:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>









































































		<span id="linhaProcessoUnificado">



























<input type="text" name="numeroDigitoAnoUnificado" maxlength="25" size="20" value="0821901-51.2018" formatType="TEXT" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" id="numeroDigitoAnoUnificado">
<input type="text" id="JTRNumeroUnificado" size="3" disabled="disabled" value="8.12"/>
<input type="text" name="foroNumeroUnificado" maxlength="4" size="3" value="0001" formatType="TEXT" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" id="foroNumeroUnificado">
<input type="hidden" name="dadosConsulta.valorConsultaNuUnificado" value="0821901-51.2018.8.12.0001" id="nuProcessoUnificadoFormatado">


<script>
	(function($){
		$(function() {
			var saj = $.saj;
			var mascaraNumeroUnificado = saj.mascaraNumeroUnificado;
			var $campoNumeroDigitoAnoUnificado = $('#numeroDigitoAnoUnificado');
			var $campoForoNumeroUnificado = $('#foroNumeroUnificado');
			var $campoJTRNumeroUnificado = $('#JTRNumeroUnificado');
			saj.configurarMascaraInput($campoForoNumeroUnificado, '0000');
			saj.configurarMascaraInput($campoNumeroDigitoAnoUnificado, mascaraNumeroUnificado, $campoForoNumeroUnificado,{
				afterPaste: afterPaste
			});
			saj.bindCamposNumeroProcesso('');

				var conteudoToolTip = '';
				if(!conteudoToolTip){
					conteudoToolTip = '<div style="width: 500px;" ><div><b>Número de Processo Unificado</b></div><div>O sistema disponibiliza facilidades no preenchimento do número unificado, seu formato é NNNNNNN-DD.AAAA.J.TR.OOOO:</div><div style="padding-top: 3px;"><b>NNNNNNN</b>: Caso o número possua zeros à esquerda o sistema preenche-os automaticamente, basta informar o número e o dígito "-" ou ".". Exemplo: ao informar "310-" o sistema irá preencher "0000310-".</div><div><b>DD</b>     : Deve ser preenchido pelo usuário.</div><div><b>AAAA</b>   : Ao informar dois dígitos para o ano o sistema completa o mesmo, basta pressionar a tecla Tab. Exemplo: ao informar "08" e "Tab" o sistema irá preencher "2008".</div><div><b>J.TR</b>    : São números fixos preenchidos pelo sistema.Exemplo: 8.99.</div><div><b>OOOO</b>   : Caso o número possua zeros à esquerda o sistema preenche-os automaticamente, basta informar o número pressionar a tecla Tab. Exemplo: ao informar "10" e "Tab" o sistema irá preencher "0010".</div></div>';
				}
				$('#numeroDigitoAnoUnificado, #foroNumeroUnificado').registrarTooltip({
					conteudoTooltip: conteudoToolTip,
					localImagensTooltip: '/cpopg5/imagens/saj',
					offsetHorizontalExtra: '',
					offsetVertficalExtra: '',
					urlConteudoTooltip: '',
					posicaoTooltip: '',
					objReferenciaPosicaoTooltip:$campoForoNumeroUnificado
				});

		});

		var afterPaste = function(textoOriginal) {
			var texto = getDigits(textoOriginal);
			if (!texto || texto.length < 16) {
				return;
			}

			var jtr = $('#JTRNumeroUnificado').val();
			jtr = getDigits(jtr);
			var jtrDigitado = texto.substring(13,16);
			var foroUnificado;
			//pega os 4 ultimos digitos, e caso o jtr colado for o mesmo, coloca os 4 no campo de foro unificado
			//se o jtr for diferente nao coloca nada no campo de foro unificado
			if (jtr == jtrDigitado) {
				foroUnificado = texto.substring(16,texto.length);
			} else {
				foroUnificado = '';
			}

			var numeroDigitoAno = texto.substring(0,13);
			var $numeroDigitoAno = $('#numeroDigitoAnoUnificado');
			$numeroDigitoAno.val(numeroDigitoAno);

			var $foroNumeroUnificado = $('#foroNumeroUnificado');
			$foroNumeroUnificado.val(foroUnificado);
			$foroNumeroUnificado.trigger('blur');
			$foroNumeroUnificado.focus();
		};

		var getDigits = function(texto) {
			return texto.replace(/[^0-9]/g, '');
		};
		$('#numeroDigitoAnoUnificado').attr('aria-label','Número do processo. Informe os treze primeiros dígitos do número do processo.');
		$('#foroNumeroUnificado').attr('aria-label','Informe os quatro últimos dígitos do número do processo.');
	})(jQuery);

</script>













		</span>


















































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'nuProcessoAntigoFormatado';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="linhaProcessoAntigo">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="25" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="nuProcessoAntigoFormatado" title="" alt="">















		</span>











			</td>
		</tr>
	  </table>







		</td>

			</tr>



















































































				<tr id="NMPARTE" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">Nome da parte:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_NMPARTE" style="display:block;font-size:0;">Nome da parte</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_NMPARTE';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled spwCampoTexto" id="campo_NMPARTE" title="" alt="">















		</span>


























<span id="">
	<label for="id_tag.checkbox.nomecompleto.rotulo">
		<input type="checkbox" name="chNmCompleto" value="true" style="vertical-align:middle;" id="id_tag.checkbox.nomecompleto.rotulo">
		Pesquisar por nome completo
	</label>
</span>




			</td>
		</tr>
	  </table>







		</td>

			</tr>













































































				<tr id="DOCPARTE" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">Documento da Parte:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_DOCPARTE" style="display:block;font-size:0;">Documento da Parte</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_DOCPARTE';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="campo_DOCPARTE" title="" alt="">















		</span>








			</td>
		</tr>
	  </table>







		</td>

			</tr>











































































				<tr id="NMADVOGADO" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">Nome do Advogado:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_NMADVOGADO" style="display:block;font-size:0;">Nome do Advogado</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_NMADVOGADO';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled spwCampoTexto" id="campo_NMADVOGADO" title="" alt="">















		</span>


























<span id="">
	<label for="id_tag.checkbox.nomecompleto.rotulo">
		<input type="checkbox" name="chNmCompleto" value="true" style="vertical-align:middle;" id="id_tag.checkbox.nomecompleto.rotulo">
		Pesquisar por nome completo
	</label>
</span>




			</td>
		</tr>
	  </table>







		</td>

			</tr>













































































				<tr id="NUMOAB" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">OAB:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_NUMOAB" style="display:block;font-size:0;">OAB</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_NUMOAB';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="campo_NUMOAB" title="" alt="">















		</span>








			</td>
		</tr>
	  </table>







		</td>

			</tr>












































































				<tr id="PRECATORIA" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">Nº da precatória:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_PRECATORIA" style="display:block;font-size:0;">Nº da precatória</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_PRECATORIA';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="campo_PRECATORIA" title="" alt="">















		</span>








			</td>
		</tr>
	  </table>







		</td>

			</tr>












































































				<tr id="DOCDELEG" class="">




		  <td id="" width="150" valign="">





		  	    <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">Nº na delegacia:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



							<label for="campo_DOCDELEG" style="display:block;font-size:0;">Nº na delegacia</label>













































































<style>
	/* remove borda vermelha de elementos required */
	input:invalid {
		box-shadow:none;
	}
</style>

<script type="text/javascript">
	(function($){
		$(function() {
			var saj = $.saj;
			var id = 'campo_DOCDELEG';
			var idObjetoReferencia = '#' + id;
			if ('' !== '' && !false) {
				$(idObjetoReferencia).registrarTooltip({
					conteudoTooltip: '',
					posicaoTooltip: 'direita',
					objReferenciaPosicaoTooltip:$(idObjetoReferencia)
				});
			}
			//remove comportamento de exibir mensagem de erro típica do html5
			$('form:visible').attr('novalidate','');
			if (''){
				$(idObjetoReferencia).attr('aria-required','true').attr('required','');
			}
		});
	})(jQuery);

</script>







































		<span id="">



	<input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="campo_DOCDELEG" title="" alt="">















		</span>








			</td>
		</tr>
	  </table>







		</td>

			</tr>


























<input id="uuidCaptcha" type="hidden" name="uuidCaptcha" value="sajcaptcha_b0faa30af0f4404b811a76c421826bdd"/>








		</table>
	</div>

















	<table id="" class="secaoBotoesBody" width="100%" style="" cellpadding="2" cellspacing="0" border="0">
		<tr>

 				<td width="150">&nbsp;</td>

			<td align="">


















	<input type="submit" name="pbEnviar" value="Pesquisar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotaoDefault " id="pbEnviar">



			</td>
		</tr>
	</table>



</form>













































<script type="text/javascript">
    (function ($) {
        $(function () {
            var captcha = $.saj.getUrlParameter('uuidCaptcha');

            if(!captcha){
                return;
            }
            var $processoPrinc = $('.processoPrinc');
            $processoPrinc.attr('href', $processoPrinc.attr('href') + '&uuidCaptcha=' + captcha);

            var $processoPaiApenso = $('.processoPaiApenso');
            $processoPaiApenso.attr('href', $processoPaiApenso.attr('href') + '&uuidCaptcha=' + captcha);

        })
    })(jQuery);
</script>

<!-- pasta digital -->

    <table width="100%" border="0" cellspacing="0" cellpadding="1">
        <tr>
            <td align="left" valign="middle" style="padding-left: 5px;">












                        <a class="linkPasta" id="linkPasta" title="Pasta digital" href="#liberarAutoPorSenha">
                            <img src="/cpopg5/imagens/icoPeticionamento.gif" border="0" style="vertical-align: -60%"/>
                            Este processo é digital. Clique aqui para visualizar os autos.
                        </a>



            </td>
        </tr>
    </table>











































	<div class="">

			<br/>














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">



					<h2 class="subtitle">
						Dados do processo

					</h2>


		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



			<br/>

		<table id="" class="secaoFormBody" width="100%" style="" cellpadding="2" cellspacing="0" border="0">
































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="dadosFmt.numero" class="labelClass" style="text-align:right;font-weight:bold;;">Processo:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>







<!-- Atributos -->











		<span class="">
			0821901-51.2018.8.12.0001
		</span>
		<span class="" >

		</span>








			</td>
		</tr>
	  </table>







		</td>

			</tr>



























































































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="numeroProcessoSeDependente" class="labelClass" style="text-align:right;font-weight:bold;;">Classe:</label>


		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



















































































		<span id="">



	<span id="" class="">Procedimento Comum Cível</span>














		</span>




&nbsp;















































































		<span id="">



	<span id="" class="">&nbsp;</span>














		</span>









			</td>
		</tr>
	  </table>







		</td>

			</tr>































































				<tr class="">





		  <td id="" width="150" valign="">

		  </td>





		    <td valign="">








	<table cellpadding="0" cellspacing="0" border="0" width="">
		<tr>
			<td>



        <span class="labelClass">Área:</span> Cível


			</td>
		</tr>
	  </table>







		</td>

			</tr>



























































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Assunto:</label>


		  </td>





		    <td valign="">








	<span id="" class="">Enquadramento</span>











		</td>

			</tr>



































































































































































































































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Distribuição:</label>


		  </td>





		    <td valign="">








	<span id="" class="">30/07/2018 às 12:39 - Automática</span>











		</td>

			</tr>























































































				<tr class="">





		  <td id="" width="150" valign="">

		  </td>





		    <td valign="">








	<span id="" class="">3ª Vara de Fazenda Pública e de Registros Públicos - Campo Grande</span>











		</td>

			</tr>























































































































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Controle:</label>


		  </td>





		    <td valign="">








	<span id="" class="">2018/000760</span>











		</td>

			</tr>




























































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Juiz:</label>


		  </td>





		    <td valign="">








	<span id="" class="">Zidiel Infantino Coutinho</span>











		</td>

			</tr>















































































































































































				<tr class="">





		  <td id="" width="150" valign="">





		  	    <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Valor da ação:</label>


		  </td>





		    <td valign="">








	<span id="" class="">R$         10.000,00</span>











		</td>

			</tr>

















































































































































































































































































		</table>
	</div>














































































<div style="padding-top: 10px;">






















<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Partes do processo

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>


	<div id="divLinksTituloBlocoPartes">












<input id="mensagemNaoExibidapartes" type="hidden" value="Exibindo todas as partes." />
<input id="linkNaoExibidopartes" type="hidden" value="Exibir somente as partes principais." />

<span id="mensagensExibindopartes" class="mensagemExibindo">Exibindo Somente as principais partes.</span> &nbsp; <a id="linkpartes" href="javascript:" class="linkNaoSelecionado" ><span id="setasDireitapartes" class="setasDireita" >&gt;&gt;</span>Exibir todas as partes.</a>

<script>
	$(function() {
		var controlarLink = function() {
			var $linkNaoExibido = $('input#linkNaoExibidopartes');
			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
			var $link = $('a#linkpartes');

			$linkNaoExibido.val($link.html());
			$link.html(conteudoLinkNaoApresentado);
		};

		var controlarMensagem = function() {
			var $mensagemNaoExibida = $('input#mensagemNaoExibidapartes');
			var $spanMensagem = $('span#mensagensExibindopartes');
			var mensagemExibida = $spanMensagem.html();
			var mensagemNaoExibida = $mensagemNaoExibida.val();

			$spanMensagem.html(mensagemNaoExibida);
			$mensagemNaoExibida.val(mensagemExibida);
		};

		var controlarMensagemLink = function() {
			controlarMensagem();
			controlarLink();
		};

		var esconderElementosExtrasMostrarDefault = function() {
			$('#tableTodasPartes').hide();
			$('#tablePartesPrincipais').show();
		};

		var mostrarElementosExtrasEsconderDefault = function() {
			$('#tablePartesPrincipais').hide();
			$('#tableTodasPartes').show();
		};

		var initPagina = function() {
			var setasDireita = '<span id="setasDireitapartes" class="setasDireita">&gt;&gt;</span>';
			var $linkEscondido = $('input#linkNaoExibidopartes');
			$linkEscondido.val(setasDireita+$linkEscondido.val());
		};

		var bindLink = function() {
			var $link = $('a#linkpartes');
			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
			$link.bind('click', controlarMensagemLink);
		};

		initPagina();
		bindLink();
		esconderElementosExtrasMostrarDefault();
	});
</script>

	</div>

<!--  cabecalho da tabela de lista (partes) -->


<!--  dados da lista partes principais (partes) -->
<table id="tablePartesPrincipais" style="margin-left:15px; margin-top:1px;" align="center" border="0" cellPadding="0" cellSpacing="0" width="98%">











<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Autora:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Leidi Silva Ormond Galvão





			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Adriana Catelan Skowronski&nbsp;


			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Ana Silvia Pessoa Salgado de Moura&nbsp;


		</td>
</tr>












<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Réu:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Estado de Mato Grosso do Sul






			<br />
			<span class="mensagemExibindo">RepreLeg:&nbsp;</span>
			Procuradoria Geral do Estado de Mato Grosso do Sul&nbsp;
   	  </td>
</tr>


</table>


	<!--  dados da lista todas as partes (partes) -->
	<table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0"  >











<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Autora:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Leidi Silva Ormond Galvão





			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Adriana Catelan Skowronski&nbsp;


			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Ana Silvia Pessoa Salgado de Moura&nbsp;


		</td>
</tr>












<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Autora:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Melissa Chaves Miranda





			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Adriana Catelan Skowronski&nbsp;


			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Ana Silvia Pessoa Salgado de Moura&nbsp;


		</td>
</tr>












<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Autora:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Ruzymar Campos de Oliveira





			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Adriana Catelan Skowronski&nbsp;


			<br />
			<span class="mensagemExibindo">Advogada:&nbsp;</span>
			Ana Silvia Pessoa Salgado de Moura&nbsp;


		</td>
</tr>












<tr class="fundoClaro">
	<td valign="top" align="right" width="141" style="padding-bottom: 5px">
		<span class="mensagemExibindo">Réu:&nbsp;</span>
	</td>
	<td width="*" align="left" style="padding-bottom: 5px">




					Estado de Mato Grosso do Sul






			<br />
			<span class="mensagemExibindo">RepreLeg:&nbsp;</span>
			Procuradoria Geral do Estado de Mato Grosso do Sul&nbsp;
   	  </td>
</tr>


	</table>













































<div style="padding-top: 10px;">





















<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Movimentações

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>


	<div id="divLinksTituloBlocoMovimentacoes">












<input id="mensagemNaoExibidamovimentacoes" type="hidden" value="Exibindo todas as movimentações." />
<input id="linkNaoExibidomovimentacoes" type="hidden" value="Listar somente as 5 últimas." />

<span id="mensagensExibindomovimentacoes" class="mensagemExibindo">Exibindo 5 últimas.</span> &nbsp; <a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado" ><span id="setasDireitamovimentacoes" class="setasDireita" >&gt;&gt;</span>Listar todas as movimentações.</a>

<script>
	$(function() {
		var controlarLink = function() {
			var $linkNaoExibido = $('input#linkNaoExibidomovimentacoes');
			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
			var $link = $('a#linkmovimentacoes');

			$linkNaoExibido.val($link.html());
			$link.html(conteudoLinkNaoApresentado);
		};

		var controlarMensagem = function() {
			var $mensagemNaoExibida = $('input#mensagemNaoExibidamovimentacoes');
			var $spanMensagem = $('span#mensagensExibindomovimentacoes');
			var mensagemExibida = $spanMensagem.html();
			var mensagemNaoExibida = $mensagemNaoExibida.val();

			$spanMensagem.html(mensagemNaoExibida);
			$mensagemNaoExibida.val(mensagemExibida);
		};

		var controlarMensagemLink = function() {
			controlarMensagem();
			controlarLink();
		};

		var esconderElementosExtrasMostrarDefault = function() {
			$('#tabelaTodasMovimentacoes').hide();
			$('#tabelaUltimasMovimentacoes').show();
		};

		var mostrarElementosExtrasEsconderDefault = function() {
			$('#tabelaUltimasMovimentacoes').hide();
			$('#tabelaTodasMovimentacoes').show();
		};

		var initPagina = function() {
			var setasDireita = '<span id="setasDireitamovimentacoes" class="setasDireita">&gt;&gt;</span>';
			var $linkEscondido = $('input#linkNaoExibidomovimentacoes');
			$linkEscondido.val(setasDireita+$linkEscondido.val());
		};

		var bindLink = function() {
			var $link = $('a#linkmovimentacoes');
			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
			$link.bind('click', controlarMensagemLink);
		};

		initPagina();
		bindLink();
		esconderElementosExtrasMostrarDefault();
	});
</script>

	</div>




<table  style="margin-left:15px; margin-top:1px;" align="center" border="0" cellPadding="0" cellSpacing="0" width="98%">


			<thead>
				<tr>
				  <th width="120" class="label" style="vertical-align: bottom">Data</th>
				  <th vAlign="middle" width="20" aria-hidden="true">&nbsp;</th>
				  <th vAlign="middle"  class="label">Movimento</th>
				</tr>
				<tr class="fundoEscuro" height="2" aria-hidden="true">
					<td></td>
					<td></td>
					<td></td>
				</tr>
			</thead>


			<tbody id="tabelaUltimasMovimentacoes">

















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		25/11/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-52715048"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-52715048"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Informação do Sistema
				</a>




		<br />
		<span style="font-style: italic;">
			PJMS - Certid&atilde;o de realiza&ccedil;&atilde;o de consulta de repeti&ccedil;a&otilde; de a&ccedil;&atilde;o
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		25/11/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Realizada pesquisa de suspeita de repetição de ação



		<br />
		<span style="font-style: italic;">
			Nenhum processo localizado
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		22/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Em Cartório-p/ Escrivão/Diretor preparar Conclusão



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		10/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.08405509-7
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o do Autor
Data: 09/10/2018 14:59

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		05/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Publicado ato publicado em data da publicação.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o :0273/2018
Data da Publica&ccedil;&atilde;o: 08/10/2018
N&uacute;mero do Di&aacute;rio: 4126
		</span>

	</td>
</tr>



			</tbody>


			<tbody style="display: none;" id="tabelaTodasMovimentacoes">

















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		25/11/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-52715048"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-52715048"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Informação do Sistema
				</a>




		<br />
		<span style="font-style: italic;">
			PJMS - Certid&atilde;o de realiza&ccedil;&atilde;o de consulta de repeti&ccedil;a&otilde; de a&ccedil;&atilde;o
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		25/11/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Realizada pesquisa de suspeita de repetição de ação



		<br />
		<span style="font-style: italic;">
			Nenhum processo localizado
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		22/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Em Cartório-p/ Escrivão/Diretor preparar Conclusão



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		10/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.08405509-7
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o do Autor
Data: 09/10/2018 14:59

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		05/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Publicado ato publicado em data da publicação.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o :0273/2018
Data da Publica&ccedil;&atilde;o: 08/10/2018
N&uacute;mero do Di&aacute;rio: 4126
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		05/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Relação encaminhada ao D.J.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o: 0273/2018
Teor do ato: Especifiquem as partes, no prazo de 05 (cinco)
dias, se h&aacute; interesse em produ&ccedil;&atilde;o de provas, indicando-as e
requerendo-as expressamente, a fim de se verificar a
pertin&ecirc;ncia e a necessidade delas. O sil&ecirc;ncio importar&aacute; no
julgamento antecipado do pedido.
Advogados(s): Ana Silvia Pessoa Salgado de Moura (OAB 7317/MS), Adriana Catelan Skowronski (OAB 10227/MS)
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		05/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Recebidos os Autos da Procuradoria do Estado



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		05/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.01094686-9
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o do Procurador da Fazenda P&uacute;blica Estadual
Data: 05/10/2018 07:43

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		04/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-52255156"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-52255156"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Certidão Cartorária
				</a>




		<br />
		<span style="font-style: italic;">
			Certid&atilde;o de Remessa da Intima&ccedil;&atilde;o para o Portal Eletr&ocirc;nico
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		04/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-52252637"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-52252637"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Expedição de Termo
				</a>




		<br />
		<span style="font-style: italic;">
			Nesta data, preparei os autos com vista a(o) Procurador(a) do Estado de Mato Grosso do Sul, atuante neste cart&oacute;rio, para ci&ecirc;ncia e/ou manifesta&ccedil;&atilde;o.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		04/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Autos entregues em carga ao Procurador do Estado



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		04/10/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Emissão da Relação



		<br />
		<span style="font-style: italic;">
			Especifiquem as partes, no prazo de 05 (cinco)
dias, se h&aacute; interesse em produ&ccedil;&atilde;o de provas, indicando-as e
requerendo-as expressamente, a fim de se verificar a
pertin&ecirc;ncia e a necessidade delas. O sil&ecirc;ncio importar&aacute; no
julgamento antecipado do pedido.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		25/09/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Recebidos os Autos do Juiz de Direito



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		25/09/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-52149834"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-52149834"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Proferido despacho de mero expediente
				</a>




		<br />
		<span style="font-style: italic;">
			Vistos. Especifiquem as partes, no prazo de 05 (cinco) dias, se h&aacute; interesse em produ&ccedil;&atilde;o de provas, indicando-as e requerendo-as expressamente, a fim de se verificar a pertin&ecirc;ncia e a necessidade delas. O sil&ecirc;ncio importar&aacute; no julgamento antecipado do pedido. I-se. C-se.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		24/09/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Em Cartório-p/ Escrivão/Diretor preparar Conclusão



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		20/09/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.08373775-5
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o do Autor
Data: 20/09/2018 14:24

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		29/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Publicado ato publicado em data da publicação.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o :0241/2018
Data da Publica&ccedil;&atilde;o: 30/08/2018
N&uacute;mero do Di&aacute;rio: 4100
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		29/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Relação encaminhada ao D.J.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o: 0241/2018
Teor do ato: Intima&ccedil;&atilde;o da parte autora para, querendo, impugnar a contesta&ccedil;&atilde;o no prazo de 15 (quinze) dias.
Advogados(s): Ana Silvia Pessoa Salgado de Moura (OAB 7317/MS), Adriana Catelan Skowronski (OAB 10227/MS)
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		28/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Emissão da Relação



		<br />
		<span style="font-style: italic;">
			Intima&ccedil;&atilde;o da parte autora para, querendo, impugnar a contesta&ccedil;&atilde;o no prazo de 15 (quinze) dias.
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		28/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Recebidos os Autos da Procuradoria do Estado



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		28/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.01063520-0
Tipo da Peti&ccedil;&atilde;o: Contesta&ccedil;&atilde;o
Data: 28/08/2018 10:26

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		14/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Publicado ato publicado em data da publicação.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o :0221/2018
Data da Publica&ccedil;&atilde;o: 15/08/2018
N&uacute;mero do Di&aacute;rio: 4089
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		14/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Relação encaminhada ao D.J.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o: 0221/2018
Teor do ato: Ante o exposto, defiro o pedido de
reconsidera&ccedil;&atilde;o de f. 228, tornando sem efeito a decis&atilde;o de
f.225/227.
Defiro &agrave; autora os benef&iacute;cios da Gratuidade da
Justi&ccedil;a, eis que satisfeitos os requisitos do art. 98 do
CPC. Anote-se e observe-se.
Deixo de designar audi&ecirc;ncia de concilia&ccedil;&atilde;o, nos termos do artigo 334, &sect; 4&ordm;, inciso II, do CPC.
Cite-se o r&eacute;u. O prazo para o oferecimento de
contesta&ccedil;&atilde;o, de trinta dias, ter&aacute; como termo inicial a data
da juntada do aviso de recebimento, com fulcro no artigo
231, I, do CPC.
Advogados(s): Ana Silvia Pessoa Salgado de Moura (OAB 7317/MS), Adriana Catelan Skowronski (OAB 10227/MS)
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51686508"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51686508"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Certidão Cartorária
				</a>




		<br />
		<span style="font-style: italic;">
			Certid&atilde;o de Remessa da Intima&ccedil;&atilde;o para o Portal Eletr&ocirc;nico
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51683595"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51683595"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Expedição de Carta de Citação
				</a>




		<br />
		<span style="font-style: italic;">
			PJMS - CGJ - Carta de Cita&ccedil;&atilde;o - Fazenda P&uacute;blica - Integra&ccedil;&atilde;o PGE (CPC 2015)
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51683582"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51683582"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Expedição de Termo
				</a>




		<br />
		<span style="font-style: italic;">
			Em 13/08/2018, procedo &agrave; cita&ccedil;&atilde;o do(a) Ilustre Procurador(a) do Estado, referente aos autos acima mencionados.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Autos entregues em carga ao Procurador do Estado



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Emissão da Relação



		<br />
		<span style="font-style: italic;">
			Ante o exposto, defiro o pedido de
reconsidera&ccedil;&atilde;o de f. 228, tornando sem efeito a decis&atilde;o de
f.225/227.
Defiro &agrave; autora os benef&iacute;cios da Gratuidade da
Justi&ccedil;a, eis que satisfeitos os requisitos do art. 98 do
CPC. Anote-se e observe-se.
Deixo de designar audi&ecirc;ncia de concilia&ccedil;&atilde;o, nos termos do artigo 334, &sect; 4&ordm;, inciso II, do CPC.
Cite-se o r&eacute;u. O prazo para o oferecimento de
contesta&ccedil;&atilde;o, de trinta dias, ter&aacute; como termo inicial a data
da juntada do aviso de recebimento, com fulcro no artigo
231, I, do CPC.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Recebidos os Autos do Juiz de Direito



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		13/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51563516"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51563516"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Recebida petição inicial
				</a>




		<br />
		<span style="font-style: italic;">
			Ante o exposto, defiro o pedido de reconsidera&ccedil;&atilde;o de f. 228, tornando sem efeito a decis&atilde;o de f.225/227. Defiro &agrave; autora os benef&iacute;cios da Gratuidade da Justi&ccedil;a, eis que satisfeitos os requisitos do art. 98 do CPC. Anote-se e observe-se. Deixo de designar audi&ecirc;ncia de concilia&ccedil;&atilde;o, nos termos do artigo 334, &sect; 4&ordm;, inciso II, do CPC. Cite-se o r&eacute;u. O prazo para o oferecimento de contesta&ccedil;&atilde;o, de trinta dias, ter&aacute; como termo inicial a data da juntada do aviso de recebimento, com fulcro no artigo 231, I, do CPC. I-se. C-se.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		01/08/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Petição Intermediária Realizada



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.08286647-0
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o do Autor
Data: 01/08/2018 09:55

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		31/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Publicado ato publicado em data da publicação.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o :0209/2018
Data da Publica&ccedil;&atilde;o: 01/08/2018
N&uacute;mero do Di&aacute;rio: 4079
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		31/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Conclusos para Despacho



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		31/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Juntada de Emenda à Inicial



		<br />
		<span style="font-style: italic;">
			N&ordm; Protocolo: WCGR.18.08285914-8
Tipo da Peti&ccedil;&atilde;o: Emenda &agrave; inicial - Faz. P&uacute;blica
Data: 31/07/2018 16:45

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		31/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Relação encaminhada ao D.J.



		<br />
		<span style="font-style: italic;">
			Rela&ccedil;&atilde;o: 0209/2018
Teor do ato: Ante todo o exposto, declino compet&ecirc;ncia para o
Juizado Especial da Fazenda P&uacute;blica de Campo Grande.
Advogados(s): Ana Silvia Pessoa Salgado de Moura (OAB 7317/MS), Adriana Catelan Skowronski (OAB 10227/MS)
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Emissão da Relação



		<br />
		<span style="font-style: italic;">
			Ante todo o exposto, declino compet&ecirc;ncia para o
Juizado Especial da Fazenda P&uacute;blica de Campo Grande.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Recebidos os Autos do Juiz de Direito



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51533780"
				title="Visualizar documento em inteiro teor"
				href="/cpopg5/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01001ZB2W0000&cdDocumento=51533780&nmRecursoAcessado=Declarada+incompet%C3%AAncia">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51533780"
					title="Visualizar documento em inteiro teor"
					href="/cpopg5/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01001ZB2W0000&cdDocumento=51533780&nmRecursoAcessado=Declarada+incompet%C3%AAncia"> Declarada incompetência
				</a>




		<br />
		<span style="font-style: italic;">
			Ante todo o exposto, declino compet&ecirc;ncia para o Juizado Especial da Fazenda P&uacute;blica de Campo Grande. I-se. C-se.
		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Conclusos para Decisão



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Remetidos os Autos da Distribuição para o Cartório



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



















<tr class="fundoClaro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">








			<a class="linkMovVincProc"
				id="linkMovVincProc-51530773"
				title="Visualizar documento em inteiro teor"
				href="#liberarAutoPorSenha">
				<img width="16" height="16" border="0" src="/cpopg5/imagens/doc2.gif" />
			</a>

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">



				<a class="linkMovVincProc"
					id="linkMovVincProc-2-51530773"
					title="Visualizar documento em inteiro teor"
					href="#liberarAutoPorSenha"> Certidão Cartorária
				</a>




		<br />
		<span style="font-style: italic;">
			PJMS - DIST - Certid&atilde;o documentos faltantes
		</span>

	</td>
</tr>



















<tr class="fundoEscuro" style="">
	<td width="120" style="vertical-align: top">
		30/07/2018
	</td>
	<td width="20" valign="top" aria-hidden="true">

	</td>
	<td style="vertical-align: top; padding-bottom: 5px">




				Processo Distribuído por Sorteio



		<br />
		<span style="font-style: italic;">

		</span>

	</td>
</tr>



			</tbody>




</table>





































<div style="padding-top: 10px;">














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Petições diversas

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>

<!-- Tabela de petições diversas -->
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1"  >


			<thead>
			    <tr class="label">
			      <th width="140"  style="text-align:left">Data</th>
			      <th width="*" >Tipo</th>
			    </tr>
			    <tr class="fundoEscuro" height="2" aria-hidden="true">
					<td></td>
					<td></td>
				</tr>
			</thead>
			<tbody>


						<tr class="fundoClaro">
							<td width="140"  style="text-align:left">
								31/07/2018
							</td>
							<td width="*">
								Emenda à inicial - Faz. Pública <br/>

							</td>
						</tr>



						<tr class="fundoEscuro">
							<td width="140"  style="text-align:left">
								01/08/2018
							</td>
							<td width="*">
								Manifestação do Autor <br/>

							</td>
						</tr>



						<tr class="fundoClaro">
							<td width="140"  style="text-align:left">
								28/08/2018
							</td>
							<td width="*">
								Contestação <br/>

							</td>
						</tr>



						<tr class="fundoEscuro">
							<td width="140"  style="text-align:left">
								20/09/2018
							</td>
							<td width="*">
								Manifestação do Autor <br/>

							</td>
						</tr>



						<tr class="fundoClaro">
							<td width="140"  style="text-align:left">
								05/10/2018
							</td>
							<td width="*">
								Manifestação do Procurador da Fazenda Pública Estadual <br/>

							</td>
						</tr>



						<tr class="fundoEscuro">
							<td width="140"  style="text-align:left">
								09/10/2018
							</td>
							<td width="*">
								Manifestação do Autor <br/>

							</td>
						</tr>


			</tbody>



</table>
<!--  Tabela de petições diversas -->




























<script type="text/javascript">
	(function($) {
		$(function(){
			var captcha = $.saj.getUrlParameter('uuidCaptcha');
			if(!captcha){
				return;
			}
			$('.incidente a').each(function(){
				var $incidente = $(this);
				var url = $incidente.attr('href');
				$incidente.attr('href', url+'&uuidCaptcha='+captcha);
			});
		})
	})(jQuery);
</script>










<div style="padding-top: 10px;">














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Incidentes, ações incidentais, recursos e execuções de sentenças

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>

<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1"  >



		<tr>
		  <td colspan="3" align="left">



 					Não há incidentes, ações incidentais, recursos ou execuções de sentenças vinculados a este processo.


		  </td>
	    </tr>


</table>
<!--  Incidentes -->




































<script type="text/javascript">
    (function ($) {
        $(function () {
            var captcha = $.saj.getUrlParameter('uuidCaptcha');

            if(!captcha){
                return;
            }
            $.each($('.processoApensado'), function (i, value) {
                var $link = $(value);
                $link.attr('href', $link.attr('href') + '&uuidCaptcha=' + captcha);
            })

        })
    })(jQuery);
</script>








<div style="padding-top: 10px;">














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Apensos, Entranhados e Unificados

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>




        <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
            <tbody id="dadosApensosNaoDisponiveis">
            <tr>
                <td colspan="3" align="left">Não há processos apensados, entranhados e unificados a este processo.</td>
            </tr>
            </tbody>
        </table>























<div style="padding-top: 10px;">














<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="21" valign="top" nowrap background="/cpopg5/imagens/spw/fundo_subtitulo.gif">


					<h2 class="subtitle">
						Audiências

					</h2>



		</td>
		<td background="/cpopg5/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
			<img src="/cpopg5/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
		</td>
	</tr>
</table>



</div>
























<a name="audienciasPlaceHolder"></a>
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">



			<tr>
			  <td colspan="3" align="left" >



			  			Não há Audiências futuras vinculadas a este processo.


			  </td>
			</tr>


</table>


















	<table id="" class="secaoBotoesBody" width="100%" style="" cellpadding="2" cellspacing="0" border="0">
		<tr>

			<td align="center">




			</td>
		</tr>
	</table>

































</td>
</tr>
</table>
<table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaRodape" summary=" ">
    <tr>
        <td class="esajCelulaRodapeCentro">
            Desenvolvido pela Softplan em parceria com o Tribunal de Justiça do Mato Grosso do Sul

        </td>
    </tr>
</table>
<link href="https://esaj.tjms.jus.br/esaj/tema/padrao/css/saj-popup-modal.css" rel="stylesheet" type="text/css">
<link href="https://esaj.tjms.jus.br/esaj/tema/padrao/css/popup-beta.css" rel="stylesheet" type="text/css">


<script>
    var appEsajLayout = appEsajLayout || {};
    appEsajLayout.tituloCertificadoDigital = 'Certificado digital';
    appEsajLayout.cliente = 'MS';
    appEsajLayout.emailParaContato = '';
    appEsajLayout.utilizarBotaoContato = 'true';
    appEsajLayout.contexto = 'https://esaj.tjms.jus.br/esaj';

    if(window.jQuery) {
        jQuery.saj = jQuery.saj || {};
        jQuery.saj.certificado = jQuery.saj.certificado || {};
        jQuery.saj.certificado.cliente = 'MS';
        jQuery.saj.certificado.tituloCertificadoDigital = 'Certificado digital';
        jQuery.saj.certificado.tituloProblemasAoAssinar = 'Falha de comunicação com o dispositivo de assinatura digital';
        jQuery.saj.certificado.urlConteudoAjudaWebSigner = appEsajLayout.contexto + '/ajudaWebSigner.do';
        jQuery.saj.certificado.licenca = 'ATsCKi50am1zLmp1cy5iciwxMC4yMC4xMDAuMTIzLDEwLjIwLjEwMC4xMjQsMTAuMjAuMTAwLjEyNSwxMC4yMC4xMDAuMTI2LDEwLjIwLjEwMC4xMjcsMTAuMjAuMTAwLjEyOCwxMC4yMC4xMDAuNzIsMTAuMjAuMTAwLjczLDEwLjIwLjEwMC43NCwxMC4yMC4xMDAuNzUsMTAuMjAuMTAwLjc2LDEwLjIwLjEwMC43NywxMC4yMC4xMDAuNzgsMTAuMjAuMTAwLjc5LDE3Mi4yMy4yMC44MSwxNzIuMjMuMjEuMTM5LDE3Mi4yMy4yMS4xNDEsMTkyLjE2OC4xLjEyMCwxOTIuMTY4LjEuMTIxLDE5Mi4xNjguMS4xOTEsMTkyLjE2OC4xLjE5MiwxOTIuMTY4LjEuNzAsMTkyLjE2OC4xLjcxLDE5Mi4xNjguMS43MiwxOTIuMTY4LjEuNzMsMTkyLjE2OC4xLjc0LDE5Mi4xNjguMS43NSwxOTIuMTY4LjEuNzYsMTkyLjE2OC4xLjc3LDE5Mi4xNjguMS43OCwxOTIuMTY4LjEuNzksMTkyLjE2OC4xLjgwLDE5Mi4xNjguMS44MSwxOTIuMTY4LjEuODIsMTkyLjE2OC4xLjgzLDE5Mi4xNjguMS44NCwxOTIuMTY4LjEuODUsMTkyLjE2OC4xLjg2LDE5Mi4xNjguMS44NywxOTIuMTY4LjEuODgsMTkyLjE2OC4xLjg5LDE5Mi4xNjguMS45MAAAAAHAmb3Vqpkj+m/wfGbysS4YZZS2uY8jnt8MjGSa/N0JmZ2hlXJ8f/ZZiDmrElNO8SNi7qztigkK3tQycbZE18+I9C1cF9YpjBigMXm+9ZiaPykVtoR8g43//Q9VUlVRj3wSF2TFLALMIn4BBETz61pmyzDzQkdX3sjFMDW6yZ9a/9eR7OisBZ9dVK8eeKe8EyskfDAKT+wdSX8zutR79RyOx9ilLgkE2g1O04nTpablXcouvirvav64ugBDiCjOtHhI5y59rFu3NBfoWo7EIq8FZr05LhAPaqujxLoQ6dtDym9g1W32wI4wMRp6EF7yepE8eXN5QEaayXZm9oDaBkoe';
        jQuery.saj.certificado.cofreDigital = jQuery.saj.certificado.cofreDigital || {};
        jQuery.saj.certificado.cofreDigital.habilitado = 'true' === 'true';
        jQuery.saj.certificado.cofreDigital.enderecoBase = 'https://esaj.tjms.jus.br/esaj';
    }

</script>
<script src="https://esaj.tjms.jus.br/esaj/js/app-bundle.js?n=447896787"></script>
<script src="https://esaj.tjms.jus.br/sajcas/seletorVersaoBeta.js?n=1b14ba90-ca20-4494-b468-7523361ddc79&versao=1"></script>
<script language="javascript" type="text/JavaScript" src="https://esaj.tjms.jus.br/esaj/js/softplan-websigner-2.5.1.js?n=736057767"></script>

<script language="javascript" type="text/JavaScript" src="https://esaj.tjms.jus.br/esaj/js/saj-certificado.js?n=2205257179"></script>



<div id="webSignerNaoInstalado" style="display: none;">
    <p>Para utilização do certificado digital no Portal e-SAJ é necessário a instalação do plug-in Web Signer. Por favor, realize a instalação antes de continuar.</p>
    <div class="footer_certificado">
        <button id="redirecionarParaPaginaInstalacao" class="actionPrincipal spwBotaoDefault">Instalar</button>
        <button class="fecharModalInstalacao spwBotao">Cancelar</button>
        <button class="spwBotao" onclick="window.open('https://esaj.tjms.jus.br/WebHelp//#id_instalacao_lacuna.htm','_blank')">Ajuda</button>
    </div>
</div>

<div id="webSignerNaoSuportado" style="display: none;">
    <p>O navegador utilizado não é compatível com a tecnologia (Web Signer) necessária para utilização do certificado digital. Por favor, utilize um dos navegadores homologados. Em caso de dúvidas, efetue a validação de requisitos <a href="https://esaj.tjms.jus.br/petpg/abrirVerificacaoRequisitosPet.do" target="_blank">aqui</a>.</p>
    <div class="footer_certificado">
        <button class="fecharModalInstalacao spwBotaoDefault actionPrincipal">OK</button>
    </div>
</div>



























	<form action="/cpopg5/show.do?processo.codigo=01001ZB2W0000&processo.foro=1&uuidCaptcha=sajcaptcha_b0faa30af0f4404b811a76c421826bdd" id="popupSenha" style="display: none;" method="POST">

		<table>


					<tr>
						<td colspan="2" style="padding-left: 20px" class="orientacao121" tabindex="2" aria-label="Atendendo o que está exposto na Res. 121 do CNJ.">
							Atendendo o que está exposto na Res. 121 do CNJ.
						</td>
					<tr>
					<tr>
						<td colspan="2" tabindex="3" aria-label="Será necessário informar uma senha para acessar processos em segredo de justiça, bem como para acessar autos dos demais processos. Caso não a possua e seja parte do processo, dirija-se ao cartório para solicitá-la.">
						<img src="/cpopg5/imagens/setaTopico.gif">
						Será necessário informar uma senha para acessar processos em segredo de justiça, bem como para acessar autos dos demais processos. Caso não a possua e seja parte do processo, dirija-se ao cartório para solicitá-la.</td>
					</tr>
					<tr>
						<td colspan="2" tabindex="4" aria-label="Se for advogado (a) neste processo habilite-se no Portal ou efetue login pelo link "Identificar-se". O número de sua OAB no cadastro do Portal deverá ser igual ao número nos dados do processo.">
						<img src="/cpopg5/imagens/setaTopico.gif">
						Se for advogado (a) neste processo habilite-se no Portal ou efetue login pelo link "Identificar-se". O número de sua OAB no cadastro do Portal deverá ser igual ao número nos dados do processo.</td>
					</tr>



			<tr align="center">
				<td align="right" width="47%"><b style="margin: 10px 0;">Senha do Processo:</b></td>
				<td align="left">
					<input type="password" name="senhaProcesso" maxlength="12" value="" rotulo="Senha do Processo" style="margin: 10px 0;" id="senhaProcesso">
					<input type="hidden" name="idRecursoQueProvocouLiberacaoPorSenha" value="">
				</td>
			</tr>
			<tr>
				<td colspan="2" align="center">




















	<input type="submit" name="btEnviarSenha" value="Continuar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotaoDefault " id="btEnviarSenha">

&nbsp;























	<input type="button" name="btFechar" value="Fechar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotao " id="botaoFecharPopupSenha">


				</td>
			</tr>
		</table>
	</form>





</div>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":101,"applicationID":"104969693","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfTxZHQRZCFkpRAkNZXw9LYFsMQSQHRAhYXg==","queueTime":0}</script></body>
</html>
"""
