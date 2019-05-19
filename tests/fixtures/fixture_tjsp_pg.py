# fmt: off
DATA = """













<html>





























































<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">










        <script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/sajcas/verificarLogin.js?script=1558158259245"></script>

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

<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(3),u=e(4),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[c.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf("Chrome")===-1&&u.indexOf("Chromium")===-1&&(o="Safari",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+x.offset],null,"api");var t=l.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===l.readyState&&i()}function i(){f("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e("handle"),c=e(3),s=e("ee"),p=e(2),d=window,l=d.document,m="addEventListener",v="attachEvent",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1123.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m]("DOMContentLoaded",i,!1),d[m]("load",r,!1)):(l[v]("onreadystatechange",o),d[v]("onload",r)),f("mark",["firstbyte",u],null,"api");var E=0,O=e(5)},{}]},{},["loader"]);</script><link rel="stylesheet" href="/cpopg/css/spw/spwConcatenado.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg/css/esaj.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg/css/saj/saj-captcha.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg/css/cpo.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg/css/formulario.css" type="text/css"/>
<link rel="stylesheet" href="/cpopg/css/saj/saj-popup-modal.css" type="text/css"/>

<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />

<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.min.js?n=c37a3c47-9a96-4308-a9b2-51033fee1244"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.func_toggle.js?n=2a35e864-d11e-4095-b35d-32714fb7e09e"></script>
<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.jplayer.2.9.2.min.js?n=c5c624d6-c5e9-428b-a4f7-382011236d37"></script>
<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.blockUI.min.js?n=5cb2a4c5-79d9-492e-be5d-d215a5f0b784"></script>
<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.browser.min.js?n=c3da14c2-e0d6-4dfb-9f4c-aafd565ac559"></script>

<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-web-2.2.41-4.js?n=f59c3370-04d3-4c58-87d2-146c9d28a5cd"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-tooltip.js?n=e2a891ad-3b88-4b38-8f17-6663f6961254"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-popup-modal-1.0.0-1.js?n=7bdecbaf-cde3-4ed2-9963-3e8f93b58709"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-browser.js?n=25fc583f-8cb4-4557-9d14-d4aef55baf7d"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-mascara-input.js?n=6d10056c-993f-4b8e-b458-cfedb1966370"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-numeroProcesso.js?n=94700c4a-f5be-4cea-b66a-9572db6bb24a"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/spw/spwConcatenado.js?n=10a4d839-f553-43fa-ba77-845e2315b7d2"></script>


<script>
        window.saj = window.saj || {};
        window.saj.env = window.saj.env || {};
        window.saj.env.root = '/cpopg';
        window.saj.env.css = '/cpopg/css';
        window.saj.env.js = '/cpopg/js';
        window.saj.env.imagens = '/cpopg/imagens';
        window.saj.env.queryString = 'processo.codigo=7J0001D040000&processo.foro=271';

        window.saj.cpo = window.saj.cpo || {};

        // transfere variavel se cpo esta rodando para totem
        window.saj.cpo.totem = 'false' == 'true';
</script>

<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj-cpo-cbpesquisa.js?n=629714429"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/formulario.js?n=1425064359"></script>
<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/acessibilidade/acessibilidade.js?n=eefb5c49-50f9-4fc8-9d91-da2e9b750465"></script>





<script>
        (function($){
                $(function(){
                        var intervalo = 1795000;
                        $.saj.manterSessao('/cpopg/manterSessao.do', intervalo);
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
    <script language="javascript" type="text/JavaScript" src="/cpopg/jsp/show-2.8.33-0.js?n=478110163"></script>






















<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<meta http-equiv="pragma" content="no-cache"/>
<meta http-equiv="cache-control" content="no-cache"/>
<meta http-equiv="expires" content="0"/>

<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/esajComum.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/esajLayout.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/css/esajLayoutSP.css" rel="stylesheet" type="text/css" />

<style type="text/css">
<!--
/* botao default means o mais claro, que seria o "botï¿½o principal" */
.spwBotaoDefault, .spwBotaoDefault-o {
        background-image: url(https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/fundoBotaoDefault.gif);
}
/* o botao secundario, menos provavel de ser clicado, mais escuro */
.spwBotao, .spwBotao-o {
        background-image: url(https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/fundoBotao.gif);
}
-->
</style>


<script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/js/menu.js?n=2553626853"></script>

<link rel="shortcut icon" href="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/favicon.ico" type="image/x-icon" />


        <script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-23111004-1']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

        </script>






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
                <td><a href="http://www.tjsp.jus.br"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/cabecalhoLogo.jpg" width="425" height="58" alt="Tribunal de Justi&ccedil;a do Estado de S&atilde;o Paulo" /></a></td>
                <td align="right" valign="top"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/cabecalhoImagem.jpg" width="353" height="58" /></td>
        </tr>
</table>





















<!-- cabecalho e-Saj -->
<table width="100%" cellpadding="0" cellspacing="0" class="esajTabelaCabecalhoServico" summary=" ">
        <tr>
                <td class="esajCelulaCabecalhoServicoLogo">




<a href="https://esaj.tjsp.jus.br/esaj/index.jsp"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/eSajServico.gif" title="Voltar para página inicial do e-SAJ" alt="Voltar para página inicial do e-SAJ" width="255" height="53" border="0" /></a><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/eSajServicoInf.gif" alt=" " width="255" height="28" border="0" /></td>
                <td class="esajCelulaCabecalhoServicoMenu">
                    <table width="100%" border="0" cellpadding="0" cellspacing="0" summary=" ">
                                <tr>
                                        <td align="right">











        <div id="divopupContato" style="display: none;">
                <div class="quadroContato"><h2>Suporte Técnico de Sistemas</h2>         <div style="text-align: left; padding: 0 20px;">             <p class="locaisContato">Cadastro de Advogados, Peticionamento Eletrônico e Processos de Primeira Instância Sistemas de 1ª Instância, Sistemas de 2ª Instância, Colégio Recursal, Consulta de Acórdão, Decisões Monocráticas, Homologações de Acordo e Jurisprudência  e Sistema Pushing.</p>             <p class="telefonesLocal"> Ligue para  0800 797 9818 (ligações gratuitas para telefones fixos) ou (11) 4199-6366 (para ligações de celulares) ou abra sua solicitação pelo portal <a target="_blank" href="http://www.suportesistemastjsp.com.br/">www.suportesistemastjsp.com.br</a></p>         </div>     </div>
        </div>


<!-- Devido ao alinhamento inline das imagens, elas não podem ter nenhum tipo de espaçamento entre elas, portanto é necessário finalizar a linha iniciando um comentário e fechar o comentário imediatamente antes da abertura da nova tag-->
<img height="24" width="47" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/inicioMenuSup.jpg"/><a href="https://esaj.tjsp.jus.br/caixapostal"><!--
--><img height="24" width="83" border="0" alt="Caixa postal" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/caixaPostal.gif"/></a><!--
--><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a href="https://esaj.tjsp.jus.br/esaj/cadastro.do"><!--
--><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/cadastro.gif" alt="Cadastro" width="81" height="24" border="0" /></a><!--

    --><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a id="linkContato" href="#"><!--
    --><img height="24" width="68" border="0" alt="Contato" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/contato.gif"/></a><!--


    --><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a target="blank" href="https://esaj.tjsp.jus.br/WebHelp/"><!--
    --><img height="24" width="61" border="0" alt="Ajuda do e-Saj" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/ajuda.gif"/></a><!--


--></td>
                                </tr>
                                <tr>
                                        <td class="esajCelulaIdentificacaoServico" >




<style>

    td.esajCelulaIdentificacao, td.esajCelulaIdentificacaoServico {
        position: relative;
    }

    button.escolhaBeta {
        border: solid 1px #aeaeae;
        background: #aeaeae;
        color: #fff;
        margin-right: 5px;
        font-family: verdana;
        font-size: 10px;
        height: 21px;
        text-transform: uppercase;
        line-height: 20px;
        border-radius: 10px;
        text-shadow: 1px 1px 1px #797979;
        position: absolute;
        top: 33px;
        right: 3px;
        padding: 0 19px;

        letter-spacing: 1px;
    }

    button.escolhaBeta:hover {
        background-color: #6c6c6c;
    }

</style>

<span id="identificacao"></span>

<button style="display: none" class="escolhaBeta"></button>






        <script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/sajcas/conteudoIdentificacao?script=1557968008261"></script>


</td>
                                </tr>
                                <tr>
                                        <td class="esajCelulaCabecalhoServicoCaminho" >












































<a href="" class="esajCaminhoLink"></a>

 &gt;


<a href="https://esaj.tjsp.jus.br/esaj/portal.do?servico=740000" class="esajCaminhoLink">Bem-vindo</a>

 &gt;


<a href="https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090" class="esajCaminhoLink">Consultas Processuais</a>

 &gt;



Consulta de Processos do 1ºGrau
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
                <a href="#" onclick="return showMenuSuspenso()"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSuspenso.gif" alt="Menu de servi&ccedil;os" width="243" height="21" style="display:block" /></a>
                <div id="layerMenu" style="display:none">


<!-- MENU -->
<ul id="esajMenuArea">
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas Processuais</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cpopg/open.do">Consulta de Processos do 1ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cposg/open.do">Consulta de Processos do 2ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cposgcr/open.do">Colégio Recursal/Turma de Uniformização</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consulta de Ordem de Processos</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do">Consulta de processos de Ordem de julgamento do 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do">Consulta de Ordem de Publicação e Cumprimento de Atos</a></li>
</ul>
  </li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Solicitação de Conciliação</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirSolicitacaoConciliacaoPreProcessual.do">Solicitação de Conciliação Pré-Processual</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Requisitórios</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Portal do Devedor</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do">Consulta de Requisitórios</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Notificação de Requisitórios</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesRequisitoriosNaoRecebidas.do">Requisitórios Pendentes de Recebimento</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesRequisitoriosRecebidas.do">Requisitórios Recebidos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaDeProcessos.do">Consulta de Processos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Notificação de Mapas Orçamentários</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesMapasOrcamentariosNaoRecebidas.do">Mapas Pendentes de Recebimento</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesMapasOrcamentariosRecebidas.do">Mapas Recebidos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirPeticionamentoIntermediario.do">Peticionamento de Intermediária</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesDocumentos.do">Notificação de Documentos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaListaPagamentos.do">Listas de Precatórios Pendentes de Pagamento e Pagamentos Disponibilizados</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaListaDepositos.do">Lista de Depósitos Efetuados</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/ctoPtl/abrirConsultaContratos.do">Contratos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas de Jurisprudência</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cjsg/consultaSimples.do">Consulta Simples</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cjsg/consultaCompleta.do">Consulta Completa</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/cdje">Diário da Justiça Eletrônico</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Biblioteca</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/obrasAbrirConsulta.do">Consulta de Obras, Periódicos e Artigos</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/jurisprudenciaAbrirConsulta.do">Jurisprudência Selecionada </a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/legislacaoAbrirConsulta.do">Consulta de Legislação e Normas</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/downloadNormasAbrirConsulta.do">Download de Normas</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/boletimAbrirConsulta.do">Boletins</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/push">Push</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões de 1º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirCadastro.do">Cadastro de Pedido de Certidão</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirConferencia.do">Conferência de Certidão</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirDownload.do">Visualizar Certidão</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões de 2º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirCadastro.do">Cadastro de Pedido de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirConferencia.do">Conferência de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirDownload.do">Download de Certidão de 2º Grau</a></li>
</ul>
  </li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Corregedoria</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cco">Consulta de Pareceres e Decisões da Corregedoria</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Conferência de Documento Digital</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/pg/abrirConferenciaDocumento.do">Conferência de Documento Digital do 1ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/sg/abrirConferenciaDocumento.do">Conferência de Documento Digital do 2ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/sgcr/abrirConferenciaDocumento.do">Conferência de Documento Digital do Colégio Recursal </a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/atendimento/abrirConferenciaDocOriginal.do">Conferência de Documento Digital de Expediente Administrativo </a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/cjpg">Consulta de Julgados de 1º Grau</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirVerificacaoRequisitosPet.do">Verificação de Requisitos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico de 1º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovaPeticaoInicial.do">Petição Inicial de 1° Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovaPeticaoIntermediaria.do">Petição Intermediária de 1° Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirConsultaPeticoes.do">Consulta de Petições de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovoComplementoProcesso.do">Complemento de Cadastro de 1º Grau</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico de 2º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirNovaPeticaoInicial.do">Peticionamento Inicial de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirConsultaPeticoes.do">Consulta de Petições de 2º Grau</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico do Colégio Recursal</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirNovaPeticaoInicial.do">Peticionamento Inicial - Colégio Recursal</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário - Colégio Recursal</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirConsultaPeticoes.do">Consulta de Petições - Colégio Recursal</a></li>
</ul>
  </li>
</ul>
  </li>
</ul>

                </div>
                </td>
                <td class="esajCelulaTituloServico"><h1 class="esajTituloPagina">Consulta de Processos do 1ºGrau</h1></td>
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
























Algumas unidades dos foros listados abaixo não estão disponíveis para consulta. Para saber quais varas estão disponíveis em cada foro clique <a style="cursor:pointer" class="layout" onclick="popup('/WebHelp/id_varas_com_pesquisa_processual_disponivel.htm','','location=no, toolbar=no, resizable=yes, width=795, height=560, scrollbars=yes')">aqui</a>.



        </li>






































        <li>
























Dúvidas? Clique <a style="cursor:pointer" class="layout" onclick="popup('/WebHelp/id_consultas_processuais.htm','','location=no, toolbar=no, resizable=yes, width=795, height=560, scrollbars=yes')">aqui</a> para mais informações sobre como pesquisar.



        </li>




















        <li>
























Processos baixados, em segredo de justiça ou distribuídos no mesmo dia serão apresentados somente na pesquisa pelo número do processo.



        </li>




            </ul>




    <br>


















<form name="consultarProcessoForm" method="GET" action="/cpopg/search.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6" autocomplete="off" enctype="" onsubmit="return applySubmit(this, eval('function spwSubmit(t, e){decodificaInputMulSelOnSubmit();if (!IS_enableSubmit) return false; return BENV_isCamposValidos(t); } spwSubmit(this, event);'));" id="formConsulta" target="">
        <input type="hidden" name="conversationId" value="">








































        <div class="">

                        <br/>














<table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr valign="top">
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">



                                        <h2 class="subtitle">
                                                Dados para pesquisa

                                        </h2>


                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
                </td>
        </tr>
</table>



                        <br/>

                <table id="secaoFormConsulta" class="secaoFormBody" width="100%" style="" cellpadding="2" cellspacing="0" border="0">




















































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="id_Foro" class="" style="text-align:right;font-weight:bold;;">Foro:</label>


                  </td>





                    <td valign="">











                <select name="dadosConsulta.localPesquisa.cdLocal" id="id_Foro" obrigatorio="" rotulo="Foro"><option value="-1">






























Todos os foros da lista abaixo

</option>

                        <option value="91">ANTIGO Foro Distrital de Brás Cubas</option>
<option value="509">Araçatuba/DEECRIM UR2</option>
<option value="26">Bauru/DEECRIM UR3</option>
<option value="502">Campinas/DEECRIM UR4</option>
<option value="500">DEPRE</option>
<option value="234">Foro - Corregedoria Geral da Justiça</option>
<option value="53">Foro Central - Fazenda Pública/Acidentes</option>
<option value="100">Foro Central Cível</option>
<option value="52">Foro Central Criminal - Juri</option>
<option value="50">Foro Central Criminal Barra Funda</option>
<option value="16">Foro Central Juizados Especiais Cíveis</option>
<option value="800">Foro da Comissão Processante Permanente</option>
<option value="14">Foro das Execuções Fiscais Estaduais</option>
<option value="90">Foro das Execuções Fiscais Municipais</option>
<option value="81">Foro de Adamantina</option>
<option value="83">Foro de Aguaí</option>
<option value="35">Foro de Águas de Lindoia</option>
<option value="58">Foro de Agudos</option>
<option value="42">Foro de Altinópolis</option>
<option value="19">Foro de Americana</option>
<option value="40">Foro de Américo Brasiliense</option>
<option value="22">Foro de Amparo</option>
<option value="24">Foro de Andradina</option>
<option value="25">Foro de Angatuba</option>
<option value="28">Foro de Aparecida</option>
<option value="30">Foro de Apiaí</option>
<option value="32">Foro de Araçatuba</option>
<option value="37">Foro de Araraquara</option>
<option value="38">Foro de Araras</option>
<option value="666">Foro de Artur Nogueira</option>
<option value="45">Foro de Arujá</option>
<option value="47">Foro de Assis</option>
<option value="48">Foro de Atibaia</option>
<option value="60">Foro de Auriflama</option>
<option value="73">Foro de Avaré</option>
<option value="59">Foro de Bananal</option>
<option value="62">Foro de Bariri</option>
<option value="63">Foro de Barra Bonita</option>
<option value="66">Foro de Barretos</option>
<option value="68">Foro de Barueri</option>
<option value="69">Foro de Bastos</option>
<option value="70">Foro de Batatais</option>
<option value="71">Foro de Bauru</option>
<option value="72">Foro de Bebedouro</option>
<option value="75">Foro de Bertioga</option>
<option value="76">Foro de Bilac</option>
<option value="77">Foro de Birigui</option>
<option value="82">Foro de Boituva</option>
<option value="67">Foro de Borborema</option>
<option value="79">Foro de Botucatu</option>
<option value="99">Foro de Bragança Paulista</option>
<option value="94">Foro de Brodowski</option>
<option value="95">Foro de Brotas</option>
<option value="691">Foro de Buri</option>
<option value="97">Foro de Buritama</option>
<option value="80">Foro de Cabreúva</option>
<option value="101">Foro de Caçapava</option>
<option value="102">Foro de Cachoeira Paulista</option>
<option value="103">Foro de Caconde</option>
<option value="104">Foro de Cafelândia</option>
<option value="106">Foro de Caieiras</option>
<option value="108">Foro de Cajamar</option>
<option value="111">Foro de Cajuru</option>
<option value="114">Foro de Campinas</option>
<option value="115">Foro de Campo Limpo Paulista</option>
<option value="116">Foro de Campos do Jordão</option>
<option value="118">Foro de Cananéia</option>
<option value="120">Foro de Cândido Mota</option>
<option value="123">Foro de Capão Bonito</option>
<option value="125">Foro de Capivari</option>
<option value="126">Foro de Caraguatatuba</option>
<option value="127">Foro de Carapicuíba</option>
<option value="128">Foro de Cardoso</option>
<option value="129">Foro de Casa Branca</option>
<option value="132">Foro de Catanduva</option>
<option value="136">Foro de Cerqueira César</option>
<option value="137">Foro de Cerquilho</option>
<option value="232">Foro de Cesário Lange</option>
<option value="140">Foro de Chavantes</option>
<option value="142">Foro de Colina</option>
<option value="144">Foro de Conchal</option>
<option value="145">Foro de Conchas</option>
<option value="146">Foro de Cordeirópolis</option>
<option value="150">Foro de Cosmópolis</option>
<option value="152">Foro de Cotia</option>
<option value="153">Foro de Cravinhos</option>
<option value="156">Foro de Cruzeiro</option>
<option value="157">Foro de Cubatão</option>
<option value="159">Foro de Cunha</option>
<option value="160">Foro de Descalvado</option>
<option value="161">Foro de Diadema</option>
<option value="165">Foro de Dois Córregos</option>
<option value="168">Foro de Dracena</option>
<option value="169">Foro de Duartina</option>
<option value="172">Foro de Eldorado Paulista</option>
<option value="176">Foro de Embu das Artes</option>
<option value="177">Foro de Embu-Guaçu</option>
<option value="180">Foro de Espírito Santo do Pinhal</option>
<option value="185">Foro de Estrela D&#39;Oeste</option>
<option value="187">Foro de Fartura</option>
<option value="189">Foro de Fernandópolis</option>
<option value="191">Foro de Ferraz de Vasconcelos</option>
<option value="673">Foro de Flórida Paulista</option>
<option value="196">Foro de Franca</option>
<option value="197">Foro de Francisco Morato</option>
<option value="198">Foro de Franco da Rocha</option>
<option value="200">Foro de Gália</option>
<option value="201">Foro de Garça</option>
<option value="204">Foro de General Salgado</option>
<option value="205">Foro de Getulina</option>
<option value="210">Foro de Guaíra</option>
<option value="213">Foro de Guará</option>
<option value="218">Foro de Guararapes</option>
<option value="219">Foro de Guararema</option>
<option value="220">Foro de Guaratinguetá</option>
<option value="222">Foro de Guariba</option>
<option value="223">Foro de Guarujá</option>
<option value="224">Foro de Guarulhos</option>
<option value="229">Foro de Hortolândia</option>
<option value="27">Foro de Iacanga</option>
<option value="233">Foro de Ibaté</option>
<option value="236">Foro de Ibitinga</option>
<option value="238">Foro de Ibiúna</option>
<option value="240">Foro de Iepê</option>
<option value="242">Foro de Igarapava</option>
<option value="244">Foro de Iguape</option>
<option value="246">Foro de Ilha Solteira</option>
<option value="247">Foro de Ilhabela</option>
<option value="248">Foro de Indaiatuba</option>
<option value="252">Foro de Ipauçu</option>
<option value="257">Foro de Ipuã</option>
<option value="262">Foro de Itaberá</option>
<option value="263">Foro de Itaí</option>
<option value="264">Foro de Itajobi</option>
<option value="266">Foro de Itanhaém</option>
<option value="268">Foro de Itapecerica da Serra</option>
<option value="269">Foro de Itapetininga</option>
<option value="270">Foro de Itapeva</option>
<option value="271" selected="selected">Foro de Itapevi</option>
<option value="272">Foro de Itapira</option>
<option value="274">Foro de Itápolis</option>
<option value="275">Foro de Itaporanga</option>
<option value="278">Foro de Itaquaquecetuba</option>
<option value="279">Foro de Itararé</option>
<option value="280">Foro de Itariri</option>
<option value="281">Foro de Itatiba</option>
<option value="282">Foro de Itatinga</option>
<option value="283">Foro de Itirapina</option>
<option value="286">Foro de Itu</option>
<option value="514">Foro de Itupeva</option>
<option value="288">Foro de Ituverava</option>
<option value="291">Foro de Jaboticabal</option>
<option value="292">Foro de Jacareí</option>
<option value="294">Foro de Jacupiranga</option>
<option value="296">Foro de Jaguariúna</option>
<option value="297">Foro de Jales</option>
<option value="299">Foro de Jandira</option>
<option value="300">Foro de Jardinópolis</option>
<option value="301">Foro de Jarinu</option>
<option value="302">Foro de Jaú</option>
<option value="306">Foro de José Bonifácio</option>
<option value="309">Foro de Jundiaí</option>
<option value="311">Foro de Junqueirópolis</option>
<option value="312">Foro de Juquiá</option>
<option value="315">Foro de Laranjal Paulista</option>
<option value="318">Foro de Leme</option>
<option value="319">Foro de Lençóis Paulista</option>
<option value="320">Foro de Limeira</option>
<option value="322">Foro de Lins</option>
<option value="323">Foro de Lorena</option>
<option value="681">Foro de Louveira</option>
<option value="326">Foro de Lucélia</option>
<option value="333">Foro de Macatuba</option>
<option value="334">Foro de Macaubal</option>
<option value="337">Foro de Mairinque</option>
<option value="338">Foro de Mairiporã</option>
<option value="341">Foro de Maracaí</option>
<option value="344">Foro de Marília</option>
<option value="346">Foro de Martinópolis</option>
<option value="347">Foro de Matão</option>
<option value="348">Foro de Mauá</option>
<option value="352">Foro de Miguelópolis</option>
<option value="355">Foro de Miracatu</option>
<option value="356">Foro de Mirandópolis</option>
<option value="357">Foro de Mirante do Paranapanema</option>
<option value="358">Foro de Mirassol</option>
<option value="360">Foro de Mococa</option>
<option value="361">Foro de Mogi das Cruzes</option>
<option value="362">Foro de Mogi Guaçu</option>
<option value="363">Foro de Mogi Mirim</option>
<option value="366">Foro de Mongaguá</option>
<option value="368">Foro de Monte Alto</option>
<option value="369">Foro de Monte Aprazível</option>
<option value="370">Foro de Monte Azul Paulista</option>
<option value="372">Foro de Monte Mor</option>
<option value="374">Foro de Morro Agudo</option>
<option value="695">Foro de Nazaré Paulista</option>
<option value="382">Foro de Neves Paulista</option>
<option value="383">Foro de Nhandeara</option>
<option value="390">Foro de Nova Granada</option>
<option value="394">Foro de Nova Odessa</option>
<option value="396">Foro de Novo Horizonte</option>
<option value="397">Foro de Nuporanga</option>
<option value="400">Foro de Olímpia</option>
<option value="404">Foro de Orlândia</option>
<option value="405">Foro de Osasco</option>
<option value="407">Foro de Osvaldo Cruz</option>
<option value="408">Foro de Ourinhos</option>
<option value="696">Foro de Ouroeste</option>
<option value="411">Foro de Pacaembu</option>
<option value="412">Foro de Palestina</option>
<option value="414">Foro de Palmeira D&#39;Oeste</option>
<option value="415">Foro de Palmital</option>
<option value="416">Foro de Panorama</option>
<option value="417">Foro de Paraguaçu Paulista</option>
<option value="418">Foro de Paraibuna</option>
<option value="420">Foro de Paranapanema</option>
<option value="424">Foro de Pariquera-Açu</option>
<option value="426">Foro de Patrocínio Paulista</option>
<option value="428">Foro de Paulínia</option>
<option value="430">Foro de Paulo de Faria</option>
<option value="431">Foro de Pederneiras</option>
<option value="434">Foro de Pedregulho</option>
<option value="435">Foro de Pedreira</option>
<option value="438">Foro de Penápolis</option>
<option value="439">Foro de Pereira Barreto</option>
<option value="441">Foro de Peruíbe</option>
<option value="443">Foro de Piedade</option>
<option value="444">Foro de Pilar do Sul</option>
<option value="445">Foro de Pindamonhangaba</option>
<option value="447">Foro de Pinhalzinho</option>
<option value="449">Foro de Piquete</option>
<option value="450">Foro de Piracaia</option>
<option value="451">Foro de Piracicaba</option>
<option value="452">Foro de Piraju</option>
<option value="453">Foro de Pirajuí</option>
<option value="698">Foro de Pirangi</option>
<option value="456">Foro de Pirapozinho</option>
<option value="457">Foro de Pirassununga</option>
<option value="458">Foro de Piratininga</option>
<option value="459">Foro de Pitangueiras</option>
<option value="462">Foro de Poá</option>
<option value="464">Foro de Pompéia</option>
<option value="466">Foro de Pontal</option>
<option value="470">Foro de Porangaba</option>
<option value="471">Foro de Porto Feliz</option>
<option value="472">Foro de Porto Ferreira</option>
<option value="474">Foro de Potirendaba</option>
<option value="477">Foro de Praia Grande</option>
<option value="480">Foro de Presidente Bernardes</option>
<option value="481">Foro de Presidente Epitácio</option>
<option value="482">Foro de Presidente Prudente</option>
<option value="483">Foro de Presidente Venceslau</option>
<option value="484">Foro de Promissão</option>
<option value="486">Foro de Quatá</option>
<option value="488">Foro de Queluz</option>
<option value="491">Foro de Rancharia</option>
<option value="493">Foro de Regente Feijó</option>
<option value="495">Foro de Registro</option>
<option value="498">Foro de Ribeirão Bonito</option>
<option value="505">Foro de Ribeirão Pires</option>
<option value="506">Foro de Ribeirão Preto</option>
<option value="510">Foro de Rio Claro</option>
<option value="511">Foro de Rio das Pedras</option>
<option value="512">Foro de Rio Grande da Serra</option>
<option value="515">Foro de Rosana</option>
<option value="516">Foro de Roseira</option>
<option value="523">Foro de Salesópolis</option>
<option value="526">Foro de Salto</option>
<option value="699">Foro de Salto de Pirapora</option>
<option value="531">Foro de Santa Adélia</option>
<option value="533">Foro de Santa Bárbara D&#39;Oeste</option>
<option value="534">Foro de Santa Branca</option>
<option value="538">Foro de Santa Cruz das Palmeiras</option>
<option value="539">Foro de Santa Cruz do Rio Pardo</option>
<option value="541">Foro de Santa Fé do Sul</option>
<option value="543">Foro de Santa Isabel</option>
<option value="547">Foro de Santa Rita do Passa Quatro</option>
<option value="549">Foro de Santa Rosa de Viterbo</option>
<option value="529">Foro de Santana de Parnaíba</option>
<option value="553">Foro de Santo Anastácio</option>
<option value="554">Foro de Santo André</option>
<option value="562">Foro de Santos</option>
<option value="563">Foro de São Bento do Sapucaí</option>
<option value="564">Foro de São Bernardo do Campo</option>
<option value="565">Foro de São Caetano do Sul</option>
<option value="566">Foro de São Carlos</option>
<option value="568">Foro de São João da Boa Vista</option>
<option value="572">Foro de São Joaquim da Barra</option>
<option value="575">Foro de São José do Rio Pardo</option>
<option value="576">Foro de São José do Rio Preto</option>
<option value="577">Foro de São José dos Campos</option>
<option value="579">Foro de São Luiz do Paraitinga</option>
<option value="581">Foro de São Manuel</option>
<option value="582">Foro de São Miguel Arcanjo</option>
<option value="584">Foro de São Pedro</option>
<option value="586">Foro de São Roque</option>
<option value="587">Foro de São Sebastião</option>
<option value="588">Foro de São Sebastião da Grama</option>
<option value="589">Foro de São Simão</option>
<option value="590">Foro de São Vicente</option>
<option value="595">Foro de Serra Negra</option>
<option value="596">Foro de Serrana</option>
<option value="597">Foro de Sertãozinho</option>
<option value="601">Foro de Socorro</option>
<option value="602">Foro de Sorocaba</option>
<option value="604">Foro de Sumaré</option>
<option value="606">Foro de Suzano</option>
<option value="607">Foro de Tabapuã</option>
<option value="609">Foro de Taboão da Serra</option>
<option value="614">Foro de Tambaú</option>
<option value="615">Foro de Tanabi</option>
<option value="619">Foro de Taquaritinga</option>
<option value="620">Foro de Taquarituba</option>
<option value="624">Foro de Tatuí</option>
<option value="625">Foro de Taubaté</option>
<option value="627">Foro de Teodoro Sampaio</option>
<option value="629">Foro de Tietê</option>
<option value="634">Foro de Tremembé</option>
<option value="637">Foro de Tupã</option>
<option value="638">Foro de Tupi Paulista</option>
<option value="642">Foro de Ubatuba</option>
<option value="646">Foro de Urânia</option>
<option value="648">Foro de Urupês</option>
<option value="650">Foro de Valinhos</option>
<option value="651">Foro de Valparaíso</option>
<option value="653">Foro de Vargem Grande do Sul</option>
<option value="654">Foro de Vargem Grande Paulista</option>
<option value="655">Foro de Várzea Paulista</option>
<option value="659">Foro de Vinhedo</option>
<option value="660">Foro de Viradouro</option>
<option value="663">Foro de Votorantim</option>
<option value="664">Foro de Votuporanga</option>
<option value="12">Foro Distrital de Parelheiros</option>
<option value="15">Foro Especial da Infância e Juventude</option>
<option value="228">Foro Plantão - 00ª CJ - Capital</option>
<option value="635">Foro Plantão - 00ª CJ - Capital EXTINTO</option>
<option value="536">Foro Plantão - 01ª CJ - Santos</option>
<option value="537">Foro Plantão - 02ª CJ - São Be. Campo</option>
<option value="540">Foro Plantão - 03ª CJ - Santo André</option>
<option value="542">Foro Plantão - 04ª CJ - Osasco</option>
<option value="544">Foro Plantão - 05ª CJ - Jundiaí</option>
<option value="545">Foro Plantão - 06ª CJ - Brag. Paulista</option>
<option value="546">Foro Plantão - 07ª CJ - Mogi Mirim</option>
<option value="548">Foro Plantão - 08ª CJ - Campinas</option>
<option value="550">Foro Plantão - 09ª CJ - Rio Claro</option>
<option value="551">Foro Plantão - 10ª CJ - Limeira</option>
<option value="552">Foro Plantão - 11ª CJ - Pirassununga</option>
<option value="555">Foro Plantão - 12ª CJ - São Carlos</option>
<option value="556">Foro Plantão - 13ª CJ - Araraquara</option>
<option value="557">Foro Plantão - 14ª CJ - Barretos</option>
<option value="558">Foro Plantão - 15ª CJ - Catanduva</option>
<option value="559">Foro Plantão - 16ª CJ - S. J. Rio Preto</option>
<option value="560">Foro Plantão - 17ª CJ - Votuporanga</option>
<option value="561">Foro Plantão - 18ª CJ - Fernandópolis</option>
<option value="567">Foro Plantão - 19ª CJ - Sorocaba</option>
<option value="569">Foro Plantão - 20ª CJ - Itu</option>
<option value="570">Foro Plantão - 21ª CJ - Registro</option>
<option value="571">Foro Plantão - 22ª CJ - Itapetininga</option>
<option value="573">Foro Plantão - 23ª CJ - Botucatu</option>
<option value="574">Foro Plantão - 24ª CJ - Avaré</option>
<option value="578">Foro Plantão - 25ª CJ - Ourinhos</option>
<option value="580">Foro Plantão - 26ª CJ - Assis</option>
<option value="583">Foro Plantão - 27ª CJ - Pre. Prudente</option>
<option value="585">Foro Plantão - 28ª CJ - Pre. Venceslau</option>
<option value="591">Foro Plantão - 29ª CJ - Dracena</option>
<option value="592">Foro Plantão - 30ª CJ - Tupã</option>
<option value="593">Foro Plantão - 31ª CJ - Marília</option>
<option value="594">Foro Plantão - 32ª CJ - Bauru</option>
<option value="598">Foro Plantão - 33ª CJ - Jaú</option>
<option value="599">Foro Plantão - 34ª CJ - Piracicaba</option>
<option value="600">Foro Plantão - 35ª CJ - Lins</option>
<option value="603">Foro Plantão - 36ª CJ - Araçatuba</option>
<option value="605">Foro Plantão - 37ª CJ - Andradina</option>
<option value="608">Foro Plantão - 38ª CJ - Franca</option>
<option value="610">Foro Plantão - 39ª CJ - Batatais</option>
<option value="611">Foro Plantão - 40ª CJ - Ituverava</option>
<option value="530">Foro Plantão - 41ª CJ - Ribeirão Preto</option>
<option value="612">Foro Plantão - 42ª CJ - Jaboticabal</option>
<option value="613">Foro Plantão - 43ª CJ - Casa Branca</option>
<option value="535">Foro Plantão - 44ª CJ - Guarulhos</option>
<option value="616">Foro Plantão - 45ª CJ - Mogi das Cruzes</option>
<option value="617">Foro Plantão - 46ª CJ - S. J. dos Campos</option>
<option value="618">Foro Plantão - 47ª CJ - Taubaté</option>
<option value="621">Foro Plantão - 48ª CJ - Guaratinguetá</option>
<option value="622">Foro Plantão - 49ª CJ - Itapeva</option>
<option value="623">Foro Plantão - 50ª CJ - S. J. Boa Vista</option>
<option value="626">Foro Plantão - 51ª CJ - Caraguatatuba</option>
<option value="628">Foro Plantão - 52ª CJ - Itapec. da Serra</option>
<option value="630">Foro Plantão - 53ª CJ - Americana</option>
<option value="631">Foro Plantão - 54ª CJ - Amparo</option>
<option value="632">Foro Plantão - 55ª CJ - Jales</option>
<option value="633">Foro Plantão - 56ª CJ - Itanhaém</option>
<option value="84">Foro Regional de Vila Mimosa</option>
<option value="1">Foro Regional I - Santana</option>
<option value="2">Foro Regional II - Santo Amaro</option>
<option value="3">Foro Regional III - Jabaquara</option>
<option value="4">Foro Regional IV - Lapa</option>
<option value="9">Foro Regional IX - Vila Prudente</option>
<option value="5">Foro Regional V - São Miguel Paulista</option>
<option value="6">Foro Regional VI - Penha de França</option>
<option value="7">Foro Regional VII - Itaquera</option>
<option value="8">Foro Regional VIII - Tatuapé</option>
<option value="10">Foro Regional X - Ipiranga</option>
<option value="11">Foro Regional XI - Pinheiros</option>
<option value="20">Foro Regional XII - Nossa Senhora do Ó</option>
<option value="704">Foro Regional XV - Butantã</option>
<option value="243">Foro UDAJ de Natividade da Serra</option>
<option value="996">Presidente Prudente/DEECRIM UR5</option>
<option value="496">Ribeirão Preto/DEECRIM UR6</option>
<option value="158">Santos/DEECRIM UR7</option>
<option value="154">São José do Rio Preto/DEECRIM UR8</option>
<option value="520">São José dos Campos/DEECRIM UR9</option>
<option value="41">São Paulo/DEECRIM UR1</option>
<option value="21">Setor de Cartas Precatórias Cíveis - Cap</option>
<option value="521">Sorocaba/DEECRIM UR10</option></select>







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

                <option value="DOCDELEG">Nº do Documento na Delegacia</option>

                <option value="NUMCDA">CDA</option></select>



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



























<input type="text" name="numeroDigitoAnoUnificado" maxlength="25" size="20" value="1002298-86.2015" formatType="TEXT" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" id="numeroDigitoAnoUnificado">
<input type="text" id="JTRNumeroUnificado" size="3" disabled="disabled" value="8.26"/>
<input type="text" name="foroNumeroUnificado" maxlength="4" size="3" value="0271" formatType="TEXT" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" id="foroNumeroUnificado">
<input type="hidden" name="dadosConsulta.valorConsultaNuUnificado" value="10022988620158260271" id="nuProcessoUnificadoFormatado">


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
                                        localImagensTooltip: '/cpopg/imagens/saj',
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












































































                                <tr id="NUMCDA" class="">




                  <td id="" width="150" valign="">





                            <label for="chNmCompleto" class="" style="text-align:right;font-weight:bold;;">CDA:</label>


                  </td>





                    <td valign="">








        <table cellpadding="0" cellspacing="0" border="0" width="">
                <tr>
                        <td>



                                                        <label for="campo_NUMCDA" style="display:block;font-size:0;">CDA</label>













































































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
                        var id = 'campo_NUMCDA';
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



        <input type="text" name="dadosConsulta.valorConsulta" size="" value="" formatType="TEXT" formato="100" obrigatorio="" rotulo="" onkeypress="CT_KPS(this, event);" onblur="CT_BLR(this);" onkeydown="CT_KDN(this, event);" onmousemove="CT_MMOV(this, event);" onmouseout="CT_MOUT(this, event);" onmouseover="CT_MOV(this, event);" onfocus="C_OFC(this, event);" disabled="disabled" style="" class="spwCampoTexto disabled " id="campo_NUMCDA" title="" alt="">















                </span>








                        </td>
                </tr>
          </table>







                </td>

                        </tr>


























<input id="uuidCaptcha" type="hidden" name="uuidCaptcha" value=""/>








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







<!-- pasta digital -->

    <table width="100%" border="0" cellspacing="0" cellpadding="1" aria-hidden="true">
        <tr>
            <td align="left" valign="middle" style="padding-left: 5px;">










                        <a class="linkPasta" id="linkPasta" title="Pasta digital" href="#liberarAutoPorSenha" aria-hidden="true" role="presentation">
                            <img src="/cpopg/imagens/icoPeticionamento.gif" border="0" style="vertical-align: -60%"/>
                            Este processo é digital. Clique aqui para visualizar os autos.
                        </a>


            </td>
        </tr>
    </table>

    <!-- link da pasta digital exibido somente para leitores de tela (deficientes visuais), neste caso o link anterior é ignorado pelo leitor
    Obs: necessário manter a table devido aos atributos de acessibilidade se comportarem adequadamente com a tabela, comportamento que não é possível colocando
    os atributos somente na tag do link-->
    <table id="pastaAcessibilidade">
        <tr>
            <td>










                        <a class="linkPasta" id="linkPastaAcessibilidade" href="#liberarAutoPorSenha&acessibilidade=true">
                            Este processo é digital. Clique aqui para visualizar os autos.
                        </a>


            </td>
        </tr>
    </table>












































        <div class="">

                        <br/>














<table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr valign="top">
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">



                                        <h2 class="subtitle">
                                                Dados do processo

                                        </h2>


                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                        1002298-86.2015.8.26.0271
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








        <span id="" class="">Franquia</span>











                </td>

                        </tr>















































































































































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Outros assuntos:</label>


                  </td>





                    <td valign="">








        <span id="" class="">Indenização por Dano Material,Indenização por Dano Moral,Obrigações,Perdas e Danos</span>











                </td>

                        </tr>





























































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Distribuição:</label>


                  </td>





                    <td valign="">








        <span id="" class="">26/05/2015 às 18:31 - Livre</span>











                </td>

                        </tr>























































































                                <tr class="">





                  <td id="" width="150" valign="">

                  </td>





                    <td valign="">








        <span id="" class="">2ª Vara Cível - Foro de Itapevi</span>











                </td>

                        </tr>























































































































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Controle:</label>


                  </td>





                    <td valign="">








        <span id="" class="">2015/001380</span>











                </td>

                        </tr>




























































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Juiz:</label>


                  </td>





                    <td valign="">








        <span id="" class="">Márcia Blanes</span>











                </td>

                        </tr>















































































































































































                                <tr class="">





                  <td id="" width="150" valign="">





                            <label for="" class="labelClass" style="text-align:right;font-weight:bold;;">Valor da ação:</label>


                  </td>





                    <td valign="">








        <span id="" class="">R$         866.000,00</span>











                </td>

                        </tr>

















































































































































































































































































                </table>
        </div>














































































<div style="padding-top: 10px;">






















<table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr valign="top">
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Partes do processo

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        DOLCE DUO COMÉRCIO VAREJISTA DE DOCES BALAS BOMBONS E SEMELHANTES LTDA ME





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;


                        <br />
                        <span class="mensagemExibindo">Advogado:&nbsp;</span>
                        Diego Gomes Dias&nbsp;


                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Karina de Almeida Batistuci&nbsp;



                        <br />
                        <span class="mensagemExibindo">Reprtate:&nbsp;</span>
                        MARIANA REBELLO MARQUES DA COSTA SANTOS&nbsp;
          </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqdo:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        FRANQUIA SHOW ASSESSORIA EM NEGÓCIOS LTDA





                        <br />
                        <span class="mensagemExibindo">Advogado:&nbsp;</span>
                        Andre Boschetti Oliva&nbsp;


                </td>
</tr>


</table>


        <!--  dados da lista todas as partes (partes) -->
        <table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0"  >











<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        DOLCE DUO COMÉRCIO VAREJISTA DE DOCES BALAS BOMBONS E SEMELHANTES LTDA ME





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;


                        <br />
                        <span class="mensagemExibindo">Advogado:&nbsp;</span>
                        Diego Gomes Dias&nbsp;


                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Karina de Almeida Batistuci&nbsp;



                        <br />
                        <span class="mensagemExibindo">Reprtate:&nbsp;</span>
                        MARIANA REBELLO MARQUES DA COSTA SANTOS&nbsp;
          </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        REBELLOS COMÉRCIO VAREJISTA DOCES BALAS BOMBONS LTDA





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;



                        <br />
                        <span class="mensagemExibindo">Reprtate:&nbsp;</span>
                        MARIANA REBELLO MARQUES DA COSTA SANTOS&nbsp;
          </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        MARIANA REBELLO MARQUES DA COSTA SANTOS





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;


                </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        FÁBIO FURQUIM DA COSTA SANTOS





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;


                </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqte:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        YARA SILVIA REBELLO





                        <br />
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                        Paula Rodrigues da Silva&nbsp;


                </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqdo:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        FRANQUIA SHOW ASSESSORIA EM NEGÓCIOS LTDA





                        <br />
                        <span class="mensagemExibindo">Advogado:&nbsp;</span>
                        Andre Boschetti Oliva&nbsp;


                </td>
</tr>












<tr class="fundoClaro">
        <td valign="top" align="right" width="141" style="padding-bottom: 5px">
                <span class="mensagemExibindo">Reqdo:&nbsp;</span>
        </td>
        <td width="*" align="left" style="padding-bottom: 5px">




                                        IBAC INDÚSTRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA





                        <br />
                        <span class="mensagemExibindo">Advogado:&nbsp;</span>
                        Andre Boschetti Oliva&nbsp;


                </td>
</tr>


        </table>













































<div style="padding-top: 10px;">





















<table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr valign="top">
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Movimentações

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                04/03/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Suspensão do Prazo



                <br />
                <span style="font-style: italic;">
                        Prazo referente ao usu&aacute;rio foi alterado para 16/07/2019 devido &agrave; altera&ccedil;&atilde;o da tabela de feriados
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/12/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Suspensão do Prazo



                <br />
                <span style="font-style: italic;">
                        Prazo referente ao usu&aacute;rio foi alterado para 15/07/2019 devido &agrave; altera&ccedil;&atilde;o da tabela de feriados
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                29/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.18.70063977-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 29/11/2018 11:41

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                14/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0520/2018
Data da Disponibiliza&ccedil;&atilde;o: 14/11/2018
Data da Publica&ccedil;&atilde;o: 21/11/2018
N&uacute;mero do Di&aacute;rio: 2700
P&aacute;gina: 444/460
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0520/2018
Teor do ato: Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Karina de Almeida Batistuci (OAB 178033/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



                        </tbody>


                        <tbody style="display: none;" id="tabelaTodasMovimentacoes">

















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                04/03/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Suspensão do Prazo



                <br />
                <span style="font-style: italic;">
                        Prazo referente ao usu&aacute;rio foi alterado para 16/07/2019 devido &agrave; altera&ccedil;&atilde;o da tabela de feriados
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/12/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Suspensão do Prazo



                <br />
                <span style="font-style: italic;">
                        Prazo referente ao usu&aacute;rio foi alterado para 15/07/2019 devido &agrave; altera&ccedil;&atilde;o da tabela de feriados
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                29/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.18.70063977-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 29/11/2018 11:41

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                14/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0520/2018
Data da Disponibiliza&ccedil;&atilde;o: 14/11/2018
Data da Publica&ccedil;&atilde;o: 21/11/2018
N&uacute;mero do Di&aacute;rio: 2700
P&aacute;gina: 444/460
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0520/2018
Teor do ato: Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Karina de Almeida Batistuci (OAB 178033/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                13/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-46307660"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-46307660"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-46286060"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-46286060"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
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




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0395/2018
Data da Disponibiliza&ccedil;&atilde;o: 28/08/2018
Data da Publica&ccedil;&atilde;o: 29/08/2018
N&uacute;mero do Di&aacute;rio: 2647
P&aacute;gina: 480/511
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                27/08/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0395/2018
Teor do ato: Vistos. Expe&ccedil;a-se nova carta precat&oacute;ria para oitiva da testemunha Peter Egmond Schimidt no endere&ccedil;o fornecido &agrave;s fls. 848. Intime-se.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Karina de Almeida Batistuci (OAB 178033/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/08/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-44123053"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=44123053&nmRecursoAcessado=Mero+expediente">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-44123053"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=44123053&nmRecursoAcessado=Mero+expediente"> Mero expediente
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos. Expe&ccedil;a-se nova carta precat&oacute;ria para oitiva da testemunha Peter Egmond Schimidt no endere&ccedil;o fornecido &agrave;s fls. 848. Intime-se.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                24/08/2018
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
                10/08/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.18.70041747-5
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 10/08/2018 14:46

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




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.18.70039106-9
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 31/07/2018 12:19

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                13/06/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Carta Precatória Juntada



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/06/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/03/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0098/2018
Data da Disponibiliza&ccedil;&atilde;o: 13/03/2018
Data da Publica&ccedil;&atilde;o: 14/03/2018
N&uacute;mero do Di&aacute;rio: 2534
P&aacute;gina: 552/585
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                12/03/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0098/2018
Teor do ato: Ci&ecirc;ncia da audi&ecirc;ncia para inquiri&ccedil;&atilde;o designada para o dia 19/04/2018 &agrave;s 16:15 no ju&iacute;zo deprecante, conforme fls. 810.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP), Diego Gomes Dias (OAB 370898/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                08/03/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-40127378"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-40127378"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato Ordinatório - Publicável
                                </a>




                <br />
                <span style="font-style: italic;">
                        Ci&ecirc;ncia da audi&ecirc;ncia para inquiri&ccedil;&atilde;o designada para o dia 19/04/2018 &agrave;s 16:15 no ju&iacute;zo deprecante, conforme fls. 810.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                08/03/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                08/03/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                06/11/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70050079-7
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 06/11/2017 15:24

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                26/10/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0570/2017
Data da Disponibiliza&ccedil;&atilde;o: 26/10/2017
Data da Publica&ccedil;&atilde;o: 27/10/2017
N&uacute;mero do Di&aacute;rio: 2458
P&aacute;gina: 457/471
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/10/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0570/2017
Teor do ato: Requerido manifestar-se, em 05 dias, sobre a juntada de documentos novos (art. 437, &sect; 1&ordm; do CPC).
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP), Diego Gomes Dias (OAB 370898/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                23/10/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-37576486"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-37576486"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Requerido manifestar-se, em 05 dias, sobre a juntada de documentos novos (art. 437, &sect; 1&ordm; do CPC).
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                03/10/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                05/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0370/2017
Data da Disponibiliza&ccedil;&atilde;o: 05/07/2017
Data da Publica&ccedil;&atilde;o: 06/07/2017
N&uacute;mero do Di&aacute;rio: 2381
P&aacute;gina: 404/440
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                05/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0370/2017
Data da Disponibiliza&ccedil;&atilde;o: 05/07/2017
Data da Publica&ccedil;&atilde;o: 06/07/2017
N&uacute;mero do Di&aacute;rio: 2381
P&aacute;gina: 404/440
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                04/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0370/2017
Teor do ato: Vistas dos autos &agrave;s partes para:Ci&ecirc;ncia da juntada dos documentos novos.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP), Diego Gomes Dias (OAB 370898/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                04/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0370/2017
Teor do ato: Instru&ccedil;&atilde;o e Julgamento - Procedimento Ordin&aacute;rio - Indeniza&ccedil;&atilde;o
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                02/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-35121877"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-35121877"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato Ordinatório - Intimação para Andamento - Autor
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistas dos autos &agrave;s partes para:Ci&ecirc;ncia da juntada dos documentos novos.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                02/07/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                30/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70021740-8
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 30/05/2017 09:37

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                26/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Termo de Audiência Digitalizado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                25/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70021023-3
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 25/05/2017 16:34

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                11/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33981701"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33981701"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Audiência Realizada
                                </a>




                <br />
                <span style="font-style: italic;">
                        Depoimento de testemunha do autor ou requerido c&iacute;vel
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                11/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33981702"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33981702"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Audiência Realizada
                                </a>




                <br />
                <span style="font-style: italic;">
                        Depoimento de testemunha do autor ou requerido c&iacute;vel
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                11/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33981698"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33981698"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Decisão
                                </a>




                <br />
                <span style="font-style: italic;">
                        Instru&ccedil;&atilde;o e Julgamento - Procedimento Ordin&aacute;rio - Indeniza&ccedil;&atilde;o
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                10/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70018450-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 10/05/2017 11:24

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                10/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70018445-3
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 10/05/2017 11:12

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                09/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70018231-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 09/05/2017 15:26

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                08/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0256/2017
Data da Disponibiliza&ccedil;&atilde;o: 08/05/2017
Data da Publica&ccedil;&atilde;o: 09/05/2017
N&uacute;mero do Di&aacute;rio: 2341
P&aacute;gina: 332/359
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                05/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0256/2017
Teor do ato: Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                05/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33876275"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33876275"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                04/05/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33837549"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33837549"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                27/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0235/2017
Data da Disponibiliza&ccedil;&atilde;o: 26/04/2017
Data da Publica&ccedil;&atilde;o: 27/04/2017
N&uacute;mero do Di&aacute;rio: 2334
P&aacute;gina: 413/432
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                27/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0235/2017
Data da Disponibiliza&ccedil;&atilde;o: 26/04/2017
Data da Publica&ccedil;&atilde;o: 27/04/2017
N&uacute;mero do Di&aacute;rio: 2334
P&aacute;gina: 413/432
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                25/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70016251-4
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 25/04/2017 17:49

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                25/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0235/2017
Teor do ato: Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                25/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0235/2017
Teor do ato: Vistos.Fls. 692/693 e 696: expe&ccedil;a-se carta precat&oacute;ria para oitiva das testemunhas da autora junto ao Ju&iacute;zo deprecante.Intime-se.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                24/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33644328"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33644328"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                20/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33579829"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33579829"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                20/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33579830"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33579830"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                20/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33579831"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33579831"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                20/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33579832"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33579832"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                19/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33568315"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=33568315&nmRecursoAcessado=Mero+expediente">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33568315"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=33568315&nmRecursoAcessado=Mero+expediente"> Mero expediente
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.Fls. 692/693 e 696: expe&ccedil;a-se carta precat&oacute;ria para oitiva das testemunhas da autora junto ao Ju&iacute;zo deprecante.Intime-se.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                19/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0218/2017
Data da Disponibiliza&ccedil;&atilde;o: 19/04/2017
Data da Publica&ccedil;&atilde;o: 20/04/2017
N&uacute;mero do Di&aacute;rio: 2330
P&aacute;gina: 459/479
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                18/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0218/2017
Teor do ato: Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                17/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33521531"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33521531"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Providencie a parte interessada distribui&ccedil;&atilde;o da Carta Precat&oacute;ria, dispon&iacute;vel para impress&atilde;o no site do TJSP, na internet, observando-se o comunicado CG n&ordm; 2290/2016, devendo instru&iacute;-la com as c&oacute;pias necess&aacute;rias e comprovar a distribui&ccedil;&atilde;o nos autos em 15 (quinze) dias. Anoto que nos termos do comunicado mencionado, tanto nos processos com justi&ccedil;a paga quanto nos processos com justi&ccedil;a gratuita, a distribui&ccedil;&atilde;o da carta precat&oacute;ria ser&aacute; feita por meio de peticionamento eletr&ocirc;nico obrigat&oacute;rio.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                17/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33467752"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33467752"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                17/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33467753"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33467753"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                17/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33467754"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33467754"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                17/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33467755"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33467755"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Precatória Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta Precat&oacute;ria - Inquiri&ccedil;&atilde;o de Testemunha
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                11/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0204/2017
Data da Disponibiliza&ccedil;&atilde;o: 11/04/2017
Data da Publica&ccedil;&atilde;o: 12/04/2017
N&uacute;mero do Di&aacute;rio: 2326
P&aacute;gina: 349/372
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                07/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0204/2017
Teor do ato: Vistas dos autos ao autor para:*Aguarde-se pelo prazo solicitado.* Decorrido o prazo, ser&aacute; o autor intimado, por mandado ou por carta, a dar andamento ao feito em 05 dias, sob pena de extin&ccedil;&atilde;o do processo (art. 485, III e &sect; 1&ordm; do CPC).
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                06/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33354647"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33354647"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistas dos autos ao autor para:*Aguarde-se pelo prazo solicitado.* Decorrido o prazo, ser&aacute; o autor intimado, por mandado ou por carta, a dar andamento ao feito em 05 dias, sob pena de extin&ccedil;&atilde;o do processo (art. 485, III e &sect; 1&ordm; do CPC).
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                06/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Designada Audiência de Instrução e Julgamento



                <br />
                <span style="font-style: italic;">
                        Instru&ccedil;&atilde;o e Julgamento
Data: 10/05/2017 Hora 16:00
Local: Sala de Audi&ecirc;ncia
Situac&atilde;o: Realizada
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                04/04/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70012902-9
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 04/04/2017 15:24

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                29/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0177/2017
Data da Disponibiliza&ccedil;&atilde;o: 29/03/2017
Data da Publica&ccedil;&atilde;o: 30/03/2017
N&uacute;mero do Di&aacute;rio: 2317
P&aacute;gina: 553/579
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                28/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0177/2017
Teor do ato: Advogado fls. 692/693 manifestar-se sobre como se dar&aacute; a intima&ccedil;&atilde;o das testemunhas.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                27/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-33106619"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-33106619"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato Ordinatório - Publicável
                                </a>




                <br />
                <span style="font-style: italic;">
                        Advogado fls. 692/693 manifestar-se sobre como se dar&aacute; a intima&ccedil;&atilde;o das testemunhas.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                23/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70011274-6
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 23/03/2017 17:28

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                23/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70011117-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 23/03/2017 12:00

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0157/2017
Data da Disponibiliza&ccedil;&atilde;o: 22/03/2017
Data da Publica&ccedil;&atilde;o: 23/03/2017
N&uacute;mero do Di&aacute;rio: 2312
P&aacute;gina: 460/483
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                21/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0157/2017
Teor do ato: Autor recolher, em 05 dias, taxa judici&aacute;ria, guia de dilig&ecirc;ncia do Oficial de Justi&ccedil;a ou guia para expedi&ccedil;&atilde;o das cartas de intima&ccedil;&atilde;o das testemunhas que ser&atilde;o ouvidas fls. 687/688.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                20/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-32955669"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-32955669"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato Ordinatório - Intimação para Andamento - Autor
                                </a>




                <br />
                <span style="font-style: italic;">
                        Autor recolher, em 05 dias, taxa judici&aacute;ria, guia de dilig&ecirc;ncia do Oficial de Justi&ccedil;a ou guia para expedi&ccedil;&atilde;o das cartas de intima&ccedil;&atilde;o das testemunhas que ser&atilde;o ouvidas fls. 687/688.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                20/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Rol de Testemunha Juntado



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.17.70010396-8
Tipo da Peti&ccedil;&atilde;o: Rol de Testemunha
Data: 20/03/2017 11:58

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                08/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0128/2017
Data da Disponibiliza&ccedil;&atilde;o: 08/03/2017
Data da Publica&ccedil;&atilde;o: 09/03/2017
N&uacute;mero do Di&aacute;rio: 2302
P&aacute;gina: 407/438
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                07/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0128/2017
Teor do ato: Vistos.DOLCE DUO COM&Eacute;RCIO E VAREJO DE DOCES LTDA ME, REBELLOS COM&Eacute;RVIO VAREJISTA DOCES BALAS BOMBONS LTDA, MARIANA REBELLO MARQUES DA COSTA SANTOS, F&Aacute;BIO FURQUIM DA COSTA SANTOS e YARA SILVIA REBELLO promoveram a presente a&ccedil;&atilde;o de indeniza&ccedil;&atilde;o por danos morais, materiais e lucros cessantes em face de FRANQUIA SHOW ASSESSORIA EM NEG&Oacute;CIOS LTDA e IBAC - IND&Uacute;STRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA, alegando, em apertada s&iacute;ntese, que adquiriam uma loja da franquia &quot;Cacau Show&quot; com investimento portentoso, e, estimulados pelas requeridas, vieram a adquirir uma segunda loja, com o compromisso da franqueadora de prestar todo o suporte necess&aacute;rio de treinamento no per&iacute;odo inicial e de manuten&ccedil;&atilde;o na administra&ccedil;&atilde;o do neg&oacute;cio durante todo o tempo do contrato. Na inicial discorrem sobre a negocia&ccedil;&atilde;o inadequada do custo de ocupa&ccedil;&atilde;o do ponto comercial, custos de implementa&ccedil;&atilde;o e capital de giro superior ao estimado; falsa estimativa de lucro; que houve v&iacute;cio de consentimento, bem como viola&ccedil;&atilde;o &agrave; boa-f&eacute; objetiva; danos morais in re ipsa; danos morais &agrave;s pessoas jur&iacute;dicas; lucros cessantes, al&eacute;m de danos materiais (fls. 01/46). Juntou procura&ccedil;&atilde;o e documentos (fls. 47/384).Foi indeferido o pedido de concess&atilde;o da gratuidade judici&aacute;ria (fls. 385), contra o qual os autores interpuseram recurso de agravo de instrumento, assim como contra a decis&atilde;o que indeferiu o pedido de diferimento do recolhimento das custas ao final (fls. 425/434 e 483/498), a ambos sendo negado provimento (fls. 461/466 e 506/508).Regularmente citadas (fls. 548), as r&eacute;s ofertaram contesta&ccedil;&atilde;o arguindo como preliminares: ilegitimidade de parte passiva da corr&eacute; IBAC; ilegitimidade de parte ativa do coautor F&aacute;bio Furquim da Costa Santos e das coautoras, as pessoas jur&iacute;dicas Dolce Duo e Rebello. No m&eacute;rito, aduziram que os contratos de franquia foram formal e regularmente rescindidos pelas autoras; que n&atilde;o houve estimativa err&ocirc;nea de custo para a implanta&ccedil;&atilde;o das lojas; que n&atilde;o houve excesso dos valores de alugueis cobrados; que n&atilde;o s&atilde;o cab&iacute;veis danos morais &agrave;s pessoas f&iacute;sicas porque tal pedido n&atilde;o est&aacute; baseado em fatos concretos; que n&atilde;o s&atilde;o cab&iacute;veis danos morais &agrave;s pessoas jur&iacute;dicas, pois em nenhum momento as r&eacute;s estimularam os autores a contrair empr&eacute;stimos; que n&atilde;o &eacute; cab&iacute;vel o pedido de lucros cessantes, pois a franqueadores jamais prometeu qualquer margem de lucratividade aos autores; do n&atilde;o cabimento da invers&atilde;o do &ocirc;nus da prova. Pugnam pela improced&ecirc;ncia dos pedidos (fls. 549/568). Juntou procura&ccedil;&atilde;o e documentos (fls. 569/657). R&eacute;plica (fls. 660/670).Instadas a manifestar eventual interesse na realiza&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o, bem como a especificarem as provas que pretendem produzir (fls. 672/673), as r&eacute;s se manifestaram &agrave;s fls. 676/678 e os autores &agrave;s fls. 679/680 dos autos.1) A designa&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o mostra-se despicienda, considerando que ambas a parte requerida se manifestou contrariamente &agrave; sua realiza&ccedil;&atilde;o, restando improv&aacute;vel, assim, a obten&ccedil;&atilde;o de composi&ccedil;&atilde;o.2) No que concerne &agrave; argui&ccedil;&atilde;o da preliminar de ilegitimidade passiva da corr&eacute; IBAC apresentada pelas requeridas, pelo fato de esta corr&eacute; n&atilde;o estar autorizada a exercer a atividade de concess&atilde;o de franquias ou licenciamento da marca &quot;Cacau Show&quot;, entendo que essa explana&ccedil;&atilde;o n&atilde;o &eacute; capaz de afastar a legitimidade da parte.V&ecirc;-se da Circular de Oferta e Franquia - COF que a corr&eacute; IBAC - Ind&uacute;stria Brasileira de Alimentos e Chocolates Ltda figura como empresa ligada &agrave; franqueadora, atuando como fabricante e fornecedora da rede &quot;Cacau Show&quot;, e, desse modo, se enquadra naquilo que a jurisprud&ecirc;ncia denomina de fornecedor aparente, fazendo parte da cadeia de consumo, de modo a incidir a regra da solidariedade prevista no art. 12 do CDC.Al&eacute;m disso, aparece como contratante e credora das r&eacute;s nos instrumentos entre elas pactuados &agrave;s fls. 82, 131/136, 166, 275/277 e 278/280, e apresenta-se como a principal revendora dos produtos da rede, sendo necess&aacute;ria a aquisi&ccedil;&atilde;o de seus produtos para o implemento da atividade comercial. O atraso no cumprimento do contrato pelos autores ensejou que a fornecedora IBAC adotasse a conduta de condicionar a entrega das mercadorias ao pagamento antecipado da d&iacute;vida, a influir no abastecimento da loja e, por consequ&ecirc;ncia, nas vendas e prov&aacute;veis lucros. Assim, integra a cadeia de consumo, e, portanto, incide a responsabilidade solid&aacute;ria.Nesse sentido:&quot;PRESTA&Ccedil;&Atilde;O DE SERVI&Ccedil;OS EDUCACIONAIS - FRANQUIA DE ESCOLA DE INFORM&Aacute;TICA FECHAMENTO ABRUPTO - FALTA DE COMUNICA&Ccedil;&Atilde;O AOS ALUNOS - LEGITIMIDADE PASSIVA AD CAUSAM DO FRANQUEADOR FORNECEDOR APARENTE - DANOS MATERIAIS E MORAIS DEVIDOS SENTEN&Ccedil;A MANTIDA - RECURSOS IMPR&Oacute;VIDOS. Perante o consumidor n&atilde;o importam as rela&ccedil;&otilde;es jur&iacute;dicas estabelecidas entre franqueado e franqueador, respondendo toda a cadeia de fornecedores&quot;. Relator(a): Renato Sartorelli; Comarca: Presidente Prudente; &Oacute;rg&atilde;o julgador: 26&ordf; C&acirc;mara de Direito Privado; 9147130-65.2005.8.26.0000, Data do julgamento: 10/08/2011; Data de registro: 15/08/2011; Outros n&uacute;meros: 992051402482.3) A preliminar de ilegitimidade ativa dos coautores F&aacute;bio Furquim da Costa Santos e das pessoas jur&iacute;dicas Dolce Duo Com&eacute;rcio Varejista de Doces Ltda ME e Rebellos Com&eacute;rvio Varejista Doces Balas Bombons Ltda. tamb&eacute;m n&atilde;o merece acolhida, tendo em vista que a empresa Dolce Duo foi constitu&iacute;da com a participa&ccedil;&atilde;o do coautor F&aacute;bio, marido da autora Mariana Rebello Marques da Costa Santos, e as duas pessoas jur&iacute;dicas foram criadas para atendimento das franquias adquiridas e impactadas pelos contratos assumidos, sendo todas as partes interessadas no desfecho desta demanda. 4) No mais, as partes encontram-se regularmente representadas. De outro lado, presentes as condi&ccedil;&otilde;es da a&ccedil;&atilde;o e os pressupostos de constitui&ccedil;&atilde;o e desenvolvimento regular do processo. Ausentes outras mat&eacute;rias preliminares a serem enfrentadas ou nulidades ou irregularidades a serem sanadas, dou o feito por saneado. 5) Inocorrentes as hip&oacute;teses dos artigos 354 ou 355 do C&oacute;digo de Processo Civil, imp&otilde;e-se a dila&ccedil;&atilde;o da instru&ccedil;&atilde;o probat&oacute;ria para o julgamento do m&eacute;rito.Passo a fixa&ccedil;&atilde;o dos pontos controvertidos.Com efeito, a controv&eacute;rsia existente sobre os pontos de fato objeto da demanda repousa no descumprimento de deveres contratuais pelos autores ou pelas r&eacute;s, especificamente, se houve ado&ccedil;&atilde;o de conduta maliciosa pelas r&eacute;s ao induzirem os autores &agrave; aquisi&ccedil;&atilde;o das franquias em raz&atilde;o de falsa estimativa positiva de lucratividade e omiss&atilde;o quanto aos verdadeiros custos operacionais do neg&oacute;cio e investimentos, sobretudo em rela&ccedil;&atilde;o &agrave; abertura da segunda loja; se houve a presta&ccedil;&atilde;o da assessoria t&eacute;cnica necess&aacute;ria &agrave; implementa&ccedil;&atilde;o da atividade comercial; se os autores foram efetivamente afetados moralmente pelo insucesso da atividade, expondo-se a situa&ccedil;&otilde;es vexat&oacute;rias perante os c&iacute;rculos sociais que frequentavam e com abalo &agrave; sua imagem credit&iacute;cia, al&eacute;m de ofensas praticadas pelas r&eacute;s; se existiram efetivamente os chamados lucros cessantes e os danos materiais apontados pelos autores no valor de R$866.000,00; se houve v&iacute;cio de consentimento dos autores, com viola&ccedil;&atilde;o da boa-f&eacute; objetiva dos autores; se a rescis&atilde;o dos contratos promovida pelos autores foi regular e expressamente dentro das previsibilidades contratuais; se houve quita&ccedil;&atilde;o geral e irrevog&aacute;vel outorgada pelas autoras; se houve excesso na cobran&ccedil;a dos alugueis; se houve ato il&iacute;cito ou descumprimento contratual a ensejar as indeniza&ccedil;&otilde;es pleiteadas.Defiro, para a solu&ccedil;&atilde;o dos pontos controvertidos, a produ&ccedil;&atilde;o da prova oral, com depoimento pessoal das partes, por meio de seus representantes legais, testemunhas e demais documentos que as partes imputarem necess&aacute;rios, desde logo, designando audi&ecirc;ncia de instru&ccedil;&atilde;o, debates e julgamento para o dia 10 de maio de 2017, &agrave;s 16:00 horas. Desde j&aacute; fica consignado que as partes dever&atilde;o depositar o rol em Cart&oacute;rio em at&eacute; dez dias a contar da publica&ccedil;&atilde;o desta decis&atilde;o, a fim de que n&atilde;o reste prejudicado o ato, com todos os requisitos do artigo 407 do C&oacute;digo de Processo Civil, sob pena de preclus&atilde;o.Eventual produ&ccedil;&atilde;o de prova consistente na realiza&ccedil;&atilde;o de per&iacute;cia cont&aacute;bil ser&aacute; aferida ap&oacute;s a produ&ccedil;&atilde;o da prova testemunhal, &agrave; discricionariedade do ju&iacute;zo.Intimem-se.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                06/03/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-32417101"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=32417101&nmRecursoAcessado=Decis%C3%A3o+de+Saneamento+do+Processo">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-32417101"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=32417101&nmRecursoAcessado=Decis%C3%A3o+de+Saneamento+do+Processo"> Decisão de Saneamento do Processo
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.DOLCE DUO COM&Eacute;RCIO E VAREJO DE DOCES LTDA ME, REBELLOS COM&Eacute;RVIO VAREJISTA DOCES BALAS BOMBONS LTDA, MARIANA REBELLO MARQUES DA COSTA SANTOS, F&Aacute;BIO FURQUIM DA COSTA SANTOS e YARA SILVIA REBELLO promoveram a presente a&ccedil;&atilde;o de indeniza&ccedil;&atilde;o por danos morais, materiais e lucros cessantes em face de FRANQUIA SHOW ASSESSORIA EM NEG&Oacute;CIOS LTDA e IBAC - IND&Uacute;STRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA, alegando, em apertada s&iacute;ntese, que adquiriam uma loja da franquia &quot;Cacau Show&quot; com investimento portentoso, e, estimulados pelas requeridas, vieram a adquirir uma segunda loja, com o compromisso da franqueadora de prestar todo o suporte necess&aacute;rio de treinamento no per&iacute;odo inicial e de manuten&ccedil;&atilde;o na administra&ccedil;&atilde;o do neg&oacute;cio durante todo o tempo do contrato. Na inicial discorrem sobre a negocia&ccedil;&atilde;o inadequada do custo de ocupa&ccedil;&atilde;o do ponto comercial, custos de implementa&ccedil;&atilde;o e capital de giro superior ao estimado; falsa estimativa de lucro; que houve v&iacute;cio de consentimento, bem como viola&ccedil;&atilde;o &agrave; boa-f&eacute; objetiva; danos morais in re ipsa; danos morais &agrave;s pessoas jur&iacute;dicas; lucros cessantes, al&eacute;m de danos materiais (fls. 01/46). Juntou procura&ccedil;&atilde;o e documentos (fls. 47/384).Foi indeferido o pedido de concess&atilde;o da gratuidade judici&aacute;ria (fls. 385), contra o qual os autores interpuseram recurso de agravo de instrumento, assim como contra a decis&atilde;o que indeferiu o pedido de diferimento do recolhimento das custas ao final (fls. 425/434 e 483/498), a ambos sendo negado provimento (fls. 461/466 e 506/508).Regularmente citadas (fls. 548), as r&eacute;s ofertaram contesta&ccedil;&atilde;o arguindo como preliminares: ilegitimidade de parte passiva da corr&eacute; IBAC; ilegitimidade de parte ativa do coautor F&aacute;bio Furquim da Costa Santos e das coautoras, as pessoas jur&iacute;dicas Dolce Duo e Rebello. No m&eacute;rito, aduziram que os contratos de franquia foram formal e regularmente rescindidos pelas autoras; que n&atilde;o houve estimativa err&ocirc;nea de custo para a implanta&ccedil;&atilde;o das lojas; que n&atilde;o houve excesso dos valores de alugueis cobrados; que n&atilde;o s&atilde;o cab&iacute;veis danos morais &agrave;s pessoas f&iacute;sicas porque tal pedido n&atilde;o est&aacute; baseado em fatos concretos; que n&atilde;o s&atilde;o cab&iacute;veis danos morais &agrave;s pessoas jur&iacute;dicas, pois em nenhum momento as r&eacute;s estimularam os autores a contrair empr&eacute;stimos; que n&atilde;o &eacute; cab&iacute;vel o pedido de lucros cessantes, pois a franqueadores jamais prometeu qualquer margem de lucratividade aos autores; do n&atilde;o cabimento da invers&atilde;o do &ocirc;nus da prova. Pugnam pela improced&ecirc;ncia dos pedidos (fls. 549/568). Juntou procura&ccedil;&atilde;o e documentos (fls. 569/657). R&eacute;plica (fls. 660/670).Instadas a manifestar eventual interesse na realiza&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o, bem como a especificarem as provas que pretendem produzir (fls. 672/673), as r&eacute;s se manifestaram &agrave;s fls. 676/678 e os autores &agrave;s fls. 679/680 dos autos.1) A designa&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o mostra-se despicienda, considerando que ambas a parte requerida se manifestou contrariamente &agrave; sua realiza&ccedil;&atilde;o, restando improv&aacute;vel, assim, a obten&ccedil;&atilde;o de composi&ccedil;&atilde;o.2) No que concerne &agrave; argui&ccedil;&atilde;o da preliminar de ilegitimidade passiva da corr&eacute; IBAC apresentada pelas requeridas, pelo fato de esta corr&eacute; n&atilde;o estar autorizada a exercer a atividade de concess&atilde;o de franquias ou licenciamento da marca &quot;Cacau Show&quot;, entendo que essa explana&ccedil;&atilde;o n&atilde;o &eacute; capaz de afastar a legitimidade da parte.V&ecirc;-se da Circular de Oferta e Franquia - COF que a corr&eacute; IBAC - Ind&uacute;stria Brasileira de Alimentos e Chocolates Ltda figura como empresa ligada &agrave; franqueadora, atuando como fabricante e fornecedora da rede &quot;Cacau Show&quot;, e, desse modo, se enquadra naquilo que a jurisprud&ecirc;ncia denomina de fornecedor aparente, fazendo parte da cadeia de consumo, de modo a incidir a regra da solidariedade prevista no art. 12 do CDC.Al&eacute;m disso, aparece como contratante e credora das r&eacute;s nos instrumentos entre elas pactuados &agrave;s fls. 82, 131/136, 166, 275/277 e 278/280, e apresenta-se como a principal revendora dos produtos da rede, sendo necess&aacute;ria a aquisi&ccedil;&atilde;o de seus produtos para o implemento da atividade comercial. O atraso no cumprimento do contrato pelos autores ensejou que a fornecedora IBAC adotasse a conduta de condicionar a entrega das mercadorias ao pagamento antecipado da d&iacute;vida, a influir no abastecimento da loja e, por consequ&ecirc;ncia, nas vendas e prov&aacute;veis lucros. Assim, integra a cadeia de consumo, e, portanto, incide a responsabilidade solid&aacute;ria.Nesse sentido:&quot;PRESTA&Ccedil;&Atilde;O DE SERVI&Ccedil;OS EDUCACIONAIS - FRANQUIA DE ESCOLA DE INFORM&Aacute;TICA FECHAMENTO ABRUPTO - FALTA DE COMUNICA&Ccedil;&Atilde;O AOS ALUNOS - LEGITIMIDADE PASSIVA AD CAUSAM DO FRANQUEADOR FORNECEDOR APARENTE - DANOS MATERIAIS E MORAIS DEVIDOS SENTEN&Ccedil;A MANTIDA - RECURSOS IMPR&Oacute;VIDOS. Perante o consumidor n&atilde;o importam as rela&ccedil;&otilde;es jur&iacute;dicas estabelecidas entre franqueado e franqueador, respondendo toda a cadeia de fornecedores&quot;. Relator(a): Renato Sartorelli; Comarca: Presidente Prudente; &Oacute;rg&atilde;o julgador: 26&ordf; C&acirc;mara de Direito Privado; 9147130-65.2005.8.26.0000, Data do julgamento: 10/08/2011; Data de registro: 15/08/2011; Outros n&uacute;meros: 992051402482.3) A preliminar de ilegitimidade ativa dos coautores F&aacute;bio Furquim da Costa Santos e das pessoas jur&iacute;dicas Dolce Duo Com&eacute;rcio Varejista de Doces Ltda ME e Rebellos Com&eacute;rvio Varejista Doces Balas Bombons Ltda. tamb&eacute;m n&atilde;o merece acolhida, tendo em vista que a empresa Dolce Duo foi constitu&iacute;da com a participa&ccedil;&atilde;o do coautor F&aacute;bio, marido da autora Mariana Rebello Marques da Costa Santos, e as duas pessoas jur&iacute;dicas foram criadas para atendimento das franquias adquiridas e impactadas pelos contratos assumidos, sendo todas as partes interessadas no desfecho desta demanda. 4) No mais, as partes encontram-se regularmente representadas. De outro lado, presentes as condi&ccedil;&otilde;es da a&ccedil;&atilde;o e os pressupostos de constitui&ccedil;&atilde;o e desenvolvimento regular do processo. Ausentes outras mat&eacute;rias preliminares a serem enfrentadas ou nulidades ou irregularidades a serem sanadas, dou o feito por saneado. 5) Inocorrentes as hip&oacute;teses dos artigos 354 ou 355 do C&oacute;digo de Processo Civil, imp&otilde;e-se a dila&ccedil;&atilde;o da instru&ccedil;&atilde;o probat&oacute;ria para o julgamento do m&eacute;rito.Passo a fixa&ccedil;&atilde;o dos pontos controvertidos.Com efeito, a controv&eacute;rsia existente sobre os pontos de fato objeto da demanda repousa no descumprimento de deveres contratuais pelos autores ou pelas r&eacute;s, especificamente, se houve ado&ccedil;&atilde;o de conduta maliciosa pelas r&eacute;s ao induzirem os autores &agrave; aquisi&ccedil;&atilde;o das franquias em raz&atilde;o de falsa estimativa positiva de lucratividade e omiss&atilde;o quanto aos verdadeiros custos operacionais do neg&oacute;cio e investimentos, sobretudo em rela&ccedil;&atilde;o &agrave; abertura da segunda loja; se houve a presta&ccedil;&atilde;o da assessoria t&eacute;cnica necess&aacute;ria &agrave; implementa&ccedil;&atilde;o da atividade comercial; se os autores foram efetivamente afetados moralmente pelo insucesso da atividade, expondo-se a situa&ccedil;&otilde;es vexat&oacute;rias perante os c&iacute;rculos sociais que frequentavam e com abalo &agrave; sua imagem credit&iacute;cia, al&eacute;m de ofensas praticadas pelas r&eacute;s; se existiram efetivamente os chamados lucros cessantes e os danos materiais apontados pelos autores no valor de R$866.000,00; se houve v&iacute;cio de consentimento dos autores, com viola&ccedil;&atilde;o da boa-f&eacute; objetiva dos autores; se a rescis&atilde;o dos contratos promovida pelos autores foi regular e expressamente dentro das previsibilidades contratuais; se houve quita&ccedil;&atilde;o geral e irrevog&aacute;vel outorgada pelas autoras; se houve excesso na cobran&ccedil;a dos alugueis; se houve ato il&iacute;cito ou descumprimento contratual a ensejar as indeniza&ccedil;&otilde;es pleiteadas.Defiro, para a solu&ccedil;&atilde;o dos pontos controvertidos, a produ&ccedil;&atilde;o da prova oral, com depoimento pessoal das partes, por meio de seus representantes legais, testemunhas e demais documentos que as partes imputarem necess&aacute;rios, desde logo, designando audi&ecirc;ncia de instru&ccedil;&atilde;o, debates e julgamento para o dia 10 de maio de 2017, &agrave;s 16:00 horas. Desde j&aacute; fica consignado que as partes dever&atilde;o depositar o rol em Cart&oacute;rio em at&eacute; dez dias a contar da publica&ccedil;&atilde;o desta decis&atilde;o, a fim de que n&atilde;o reste prejudicado o ato, com todos os requisitos do artigo 407 do C&oacute;digo de Processo Civil, sob pena de preclus&atilde;o.Eventual produ&ccedil;&atilde;o de prova consistente na realiza&ccedil;&atilde;o de per&iacute;cia cont&aacute;bil ser&aacute; aferida ap&oacute;s a produ&ccedil;&atilde;o da prova testemunhal, &agrave; discricionariedade do ju&iacute;zo.Intimem-se.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                18/01/2017
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
                18/01/2017
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Conclusos para Sentença



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                05/12/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70036647-0
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 05/12/2016 18:11

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                01/12/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70036263-6
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 01/12/2016 17:22

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                23/11/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0369/2016
Data da Disponibiliza&ccedil;&atilde;o: 23/11/2016
Data da Publica&ccedil;&atilde;o: 24/11/2016
N&uacute;mero do Di&aacute;rio: 2245
P&aacute;gina: 583/639
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                23/11/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0369/2016
Data da Disponibiliza&ccedil;&atilde;o: 23/11/2016
Data da Publica&ccedil;&atilde;o: 24/11/2016
N&uacute;mero do Di&aacute;rio: 2245
P&aacute;gina: 583/639
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/11/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0369/2016
Teor do ato: Vistos.1) Digam as partes, em 10 dias, se possuem interesse na designa&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o.2) Sem preju&iacute;zo, faculto &agrave;s partes o prazo comum de 5 (cinco) dias para que apontem, de maneira clara, objetiva e sucinta, as quest&otilde;es de fato e de direito que entendam pertinentes ao julgamento da lide.Quanto &agrave;s quest&otilde;es de fato, dever&atilde;o indicar a mat&eacute;ria que consideram incontroversa, bem como aquela que entendem j&aacute; provada pela prova trazida, enumerando nos autos os documentos que servem de suporte a cada alega&ccedil;&atilde;o.Com rela&ccedil;&atilde;o ao restante, remanescendo controvertida, dever&atilde;o especificar as provas que pretendem produzir, justificando, objetiva e fundamentadamente, sua relev&acirc;ncia e pertin&ecirc;ncia.O sil&ecirc;ncio ou o protesto gen&eacute;rico por produ&ccedil;&atilde;o de provas ser&atilde;o interpretados como anu&ecirc;ncia ao julgamento antecipado, indeferindo-se, ainda, os requerimentos de dilig&ecirc;ncias in&uacute;teis ou meramente protelat&oacute;rias.Quanto &agrave;s quest&otilde;es de direito, para que n&atilde;o se alegue preju&iacute;zo, dever&atilde;o, desde logo, manifestar-se sobre a mat&eacute;ria cognosc&iacute;vel de of&iacute;cio pelo ju&iacute;zo, desde que interessem ao processo.Com rela&ccedil;&atilde;o aos argumentos jur&iacute;dicos trazidos pelas partes, dever&atilde;o estar de acordo com toda a legisla&ccedil;&atilde;o vigente, que, presume-se, tenha sido estudada at&eacute; o esgotamento pelos litigantes, e cujo desconhecimento n&atilde;o poder&aacute; ser posteriormente alegado.Registre-se, ainda, que n&atilde;o ser&atilde;o consideradas relevantes as quest&otilde;es n&atilde;o adequadamente delineadas e fundamentadas nas pe&ccedil;as processuais, al&eacute;m de todos os demais argumentos insubsistentes ou ultrapassados pela jurisprud&ecirc;ncia reiterada.3) Em obedi&ecirc;ncia ao princ&iacute;pio da economia processual, as partes que pretenderem produzir prova testemunhal, dever&atilde;o, no mesmo prazo, contados da intima&ccedil;&atilde;o da presente decis&atilde;o, depositar o rol das testemunhas cuja oitiva pretendem, observando-se o n&uacute;mero legal e informando se as testemunhas comparecer&atilde;o mediante intima&ccedil;&atilde;o, fornecendo desde j&aacute; o endere&ccedil;o ou independentemente de tal formalidade, presumindo-se, no sil&ecirc;ncio, a desnecessidade da intima&ccedil;&atilde;o.Ficam as partes advertidas de que a n&atilde;o apresenta&ccedil;&atilde;o do rol no prazo indicado acarretar&aacute; a preclus&atilde;o da oportunidade de produzir prova testemunhal e tornar&aacute; prejudicada a an&aacute;lise de tal pedido quando do eventual despacho saneador.Int.
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/11/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0369/2016
Teor do ato: Ag. Minuta
Advogados(s): Andre Boschetti Oliva (OAB 149247/SP), Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                20/11/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-30832612"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=30832612&nmRecursoAcessado=Mero+expediente">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-30832612"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=30832612&nmRecursoAcessado=Mero+expediente"> Mero expediente
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.1) Digam as partes, em 10 dias, se possuem interesse na designa&ccedil;&atilde;o de audi&ecirc;ncia de tentativa de concilia&ccedil;&atilde;o.2) Sem preju&iacute;zo, faculto &agrave;s partes o prazo comum de 5 (cinco) dias para que apontem, de maneira clara, objetiva e sucinta, as quest&otilde;es de fato e de direito que entendam pertinentes ao julgamento da lide.Quanto &agrave;s quest&otilde;es de fato, dever&atilde;o indicar a mat&eacute;ria que consideram incontroversa, bem como aquela que entendem j&aacute; provada pela prova trazida, enumerando nos autos os documentos que servem de suporte a cada alega&ccedil;&atilde;o.Com rela&ccedil;&atilde;o ao restante, remanescendo controvertida, dever&atilde;o especificar as provas que pretendem produzir, justificando, objetiva e fundamentadamente, sua relev&acirc;ncia e pertin&ecirc;ncia.O sil&ecirc;ncio ou o protesto gen&eacute;rico por produ&ccedil;&atilde;o de provas ser&atilde;o interpretados como anu&ecirc;ncia ao julgamento antecipado, indeferindo-se, ainda, os requerimentos de dilig&ecirc;ncias in&uacute;teis ou meramente protelat&oacute;rias.Quanto &agrave;s quest&otilde;es de direito, para que n&atilde;o se alegue preju&iacute;zo, dever&atilde;o, desde logo, manifestar-se sobre a mat&eacute;ria cognosc&iacute;vel de of&iacute;cio pelo ju&iacute;zo, desde que interessem ao processo.Com rela&ccedil;&atilde;o aos argumentos jur&iacute;dicos trazidos pelas partes, dever&atilde;o estar de acordo com toda a legisla&ccedil;&atilde;o vigente, que, presume-se, tenha sido estudada at&eacute; o esgotamento pelos litigantes, e cujo desconhecimento n&atilde;o poder&aacute; ser posteriormente alegado.Registre-se, ainda, que n&atilde;o ser&atilde;o consideradas relevantes as quest&otilde;es n&atilde;o adequadamente delineadas e fundamentadas nas pe&ccedil;as processuais, al&eacute;m de todos os demais argumentos insubsistentes ou ultrapassados pela jurisprud&ecirc;ncia reiterada.3) Em obedi&ecirc;ncia ao princ&iacute;pio da economia processual, as partes que pretenderem produzir prova testemunhal, dever&atilde;o, no mesmo prazo, contados da intima&ccedil;&atilde;o da presente decis&atilde;o, depositar o rol das testemunhas cuja oitiva pretendem, observando-se o n&uacute;mero legal e informando se as testemunhas comparecer&atilde;o mediante intima&ccedil;&atilde;o, fornecendo desde j&aacute; o endere&ccedil;o ou independentemente de tal formalidade, presumindo-se, no sil&ecirc;ncio, a desnecessidade da intima&ccedil;&atilde;o.Ficam as partes advertidas de que a n&atilde;o apresenta&ccedil;&atilde;o do rol no prazo indicado acarretar&aacute; a preclus&atilde;o da oportunidade de produzir prova testemunhal e tornar&aacute; prejudicada a an&aacute;lise de tal pedido quando do eventual despacho saneador.Int.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                10/11/2016
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



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                29/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Despacho



                <br />
                <span style="font-style: italic;">
                        Ag. Minuta
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                26/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Réplica Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70024356-4
Tipo da Peti&ccedil;&atilde;o: Manifesta&ccedil;&atilde;o Sobre a Contesta&ccedil;&atilde;o
Data: 26/08/2016 19:04

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                04/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0152/2016
Data da Disponibiliza&ccedil;&atilde;o: 04/08/2016
Data da Publica&ccedil;&atilde;o: 05/08/2016
N&uacute;mero do Di&aacute;rio: 2172
P&aacute;gina: 327/354
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                03/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0152/2016
Teor do ato: Vistas dos autos ao autor para:(x) manifestar-se, em 15 dias, sobre a contesta&ccedil;&atilde;o (art. 350 ou 351 do CPC).
Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                02/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-28855719"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-28855719"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistas dos autos ao autor para:(x) manifestar-se, em 15 dias, sobre a contesta&ccedil;&atilde;o (art. 350 ou 351 do CPC).
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                01/08/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Contestação Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70020935-8
Tipo da Peti&ccedil;&atilde;o: Contesta&ccedil;&atilde;o
Data: 01/08/2016 17:57

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                12/07/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                AR Positivo Juntado



                <br />
                <span style="font-style: italic;">
                        Juntada de AR : AR475660419TJ
Situa&ccedil;&atilde;o : Cumprido
Modelo : Processo Digital - Carta  - Cita&ccedil;&atilde;o - Rito Comum - Sem Audi&ecirc;ncia - C&iacute;vel - NOVO CPC
Destinat&aacute;rio : FRANQUIA SHOW ASSESSORIA EM NEG&Oacute;CIOS LTDA
Dilig&ecirc;ncia : 07/07/2016
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                04/07/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0095/2016
Data da Disponibiliza&ccedil;&atilde;o: 04/07/2016
Data da Publica&ccedil;&atilde;o: 05/07/2016
N&uacute;mero do Di&aacute;rio: 2149
P&aacute;gina: 316/369
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                03/07/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-28224924"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-28224924"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Carta Expedida
                                </a>




                <br />
                <span style="font-style: italic;">
                        Processo Digital - Carta - Cita&ccedil;&atilde;o - Rito Comum - Sem Audi&ecirc;ncia - C&iacute;vel - NOVO CPC
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                01/07/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0095/2016
Teor do ato: Vistos.I. Ciente do ac&oacute;rd&atilde;o que j&aacute; transitou em julgado, bem como do recolhimento das custas devidas.II. Considerando que a Comarca de Itapevi conta com poucos conciliadores no CEJUSC, revelando uma estrutura insuficiente, frente ao volume de audi&ecirc;ncias pr&eacute;vias de concilia&ccedil;&atilde;o, conforme determina o C&oacute;digo de Processo Civil, verifico a inviabilidade de sua designa&ccedil;&atilde;o nesses autos.Al&eacute;m disso, h&aacute; que se fazer uma racionaliza&ccedil;&atilde;o dos trabalhos a fim de destinar &agrave;s audi&ecirc;ncia de concilia&ccedil;&atilde;o aos casos que h&aacute; maior chance de &ecirc;xito na autocomposi&ccedil;&atilde;oAssim, diante das especificidades da causa e de modo a adequar o rito processual &agrave;s necessidade do conflito, deixo para momento oportuno a an&aacute;lise da conveni&ecirc;ncia da audi&ecirc;ncia de concilia&ccedil;&atilde;o (CPC, art. 139, VI e Enunciado n.35 da ENFAM).CITE-SE a(o) r&eacute;(u) para os termos da a&ccedil;&atilde;o em ep&iacute;grafe, cuja c&oacute;pia da inicial segue em anexo, ficando advertida(o) do prazo de 15 (quinze) dias &uacute;teis para apresentar a defesa, sob pena de serem presumidos como verdadeiros os fatos articulados na inicial, nos termos do artigo 344 do C&oacute;digo de Processo Civil.Intime-se.
Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                24/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-28088414"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=28088414&nmRecursoAcessado=Recebida+a+Peti%C3%A7%C3%A3o+Inicial++-+Cita%C3%A7%C3%A3o+Por+Carta+AR">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-28088414"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=28088414&nmRecursoAcessado=Recebida+a+Peti%C3%A7%C3%A3o+Inicial++-+Cita%C3%A7%C3%A3o+Por+Carta+AR"> Recebida a Petição Inicial  - Citação Por Carta AR
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.I. Ciente do ac&oacute;rd&atilde;o que j&aacute; transitou em julgado, bem como do recolhimento das custas devidas.II. Considerando que a Comarca de Itapevi conta com poucos conciliadores no CEJUSC, revelando uma estrutura insuficiente, frente ao volume de audi&ecirc;ncias pr&eacute;vias de concilia&ccedil;&atilde;o, conforme determina o C&oacute;digo de Processo Civil, verifico a inviabilidade de sua designa&ccedil;&atilde;o nesses autos.Al&eacute;m disso, h&aacute; que se fazer uma racionaliza&ccedil;&atilde;o dos trabalhos a fim de destinar &agrave;s audi&ecirc;ncia de concilia&ccedil;&atilde;o aos casos que h&aacute; maior chance de &ecirc;xito na autocomposi&ccedil;&atilde;oAssim, diante das especificidades da causa e de modo a adequar o rito processual &agrave;s necessidade do conflito, deixo para momento oportuno a an&aacute;lise da conveni&ecirc;ncia da audi&ecirc;ncia de concilia&ccedil;&atilde;o (CPC, art. 139, VI e Enunciado n.35 da ENFAM).CITE-SE a(o) r&eacute;(u) para os termos da a&ccedil;&atilde;o em ep&iacute;grafe, cuja c&oacute;pia da inicial segue em anexo, ficando advertida(o) do prazo de 15 (quinze) dias &uacute;teis para apresentar a defesa, sob pena de serem presumidos como verdadeiros os fatos articulados na inicial, nos termos do artigo 344 do C&oacute;digo de Processo Civil.Intime-se.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
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



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/06/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Documento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                12/04/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70009054-7
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 12/04/2016 17:24

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70001423-9
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 22/01/2016 15:25

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0010/2016
Data da Disponibiliza&ccedil;&atilde;o: 22/01/2016
Data da Publica&ccedil;&atilde;o: 25/01/2016
N&uacute;mero do Di&aacute;rio: 2042
P&aacute;gina: 435/454
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                21/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0010/2016
Teor do ato: Vistos.
Aguarde-se decis&atilde;o ou pedido de informa&ccedil;&otilde;es do agravo interposto (fls. 483/498).
Intime-se.


Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                20/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Mensagem Eletrônica (e-mail) Juntada



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                19/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-25499498"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=25499498&nmRecursoAcessado=Decis%C3%A3o">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-25499498"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=25499498&nmRecursoAcessado=Decis%C3%A3o"> Decisão
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.
Aguarde-se decis&atilde;o ou pedido de informa&ccedil;&otilde;es do agravo interposto (fls. 483/498).
Intime-se.


                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                09/01/2016
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.16.70000175-7
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&atilde;o Juntando C&oacute;pia do Agravo (Art. 526, do CPC)
Data: 08/01/2016 14:07

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                18/12/2015
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
                15/12/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Pedido de Sobrestamento Juntado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                09/12/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0190/2015
Data da Disponibiliza&ccedil;&atilde;o: 09/12/2015
Data da Publica&ccedil;&atilde;o: 10/12/2015
N&uacute;mero do Di&aacute;rio: 2023
P&aacute;gina: 376/404
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                07/12/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0190/2015
Teor do ato: Vistos.
Fls. 458/460: indefiro o pedido de diferimento do pagamento das custas, pois tal benef&iacute;cio somente &eacute; concedido nas a&ccedil;&otilde;es indicadas no rol taxativo do art. 5&ordm; da Lei n. 11.608/03, n&atilde;o se subsumindo a presente a&ccedil;&atilde;o em nenhuma das hip&oacute;teses legais. 
Desta forma e considerando ainda que o  recurso de Agravo de Instrumento interposto pleiteando os benef&iacute;cios da Justi&ccedil;a Gratuita teve seu provimento negado (fls. 461/466) dever&atilde;o os autores, no prazo de 10 dias, recolher as custas iniciais e demais despesas sob pena de cancelamento da distribui&ccedil;&atilde;o.
Sem preju&iacute;zo, providencie a serventia o desentranhamento da peti&ccedil;&atilde;o de fls. 467, bem como os documentos de fls. 468/478, uma vez que estranhos aos autos.
                Intime-se.


Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                04/12/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-25115721"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=25115721&nmRecursoAcessado=Decis%C3%A3o">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-25115721"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=25115721&nmRecursoAcessado=Decis%C3%A3o"> Decisão
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.
Fls. 458/460: indefiro o pedido de diferimento do pagamento das custas, pois tal benef&iacute;cio somente &eacute; concedido nas a&ccedil;&otilde;es indicadas no rol taxativo do art. 5&ordm; da Lei n. 11.608/03, n&atilde;o se subsumindo a presente a&ccedil;&atilde;o em nenhuma das hip&oacute;teses legais. 
Desta forma e considerando ainda que o  recurso de Agravo de Instrumento interposto pleiteando os benef&iacute;cios da Justi&ccedil;a Gratuita teve seu provimento negado (fls. 461/466) dever&atilde;o os autores, no prazo de 10 dias, recolher as custas iniciais e demais despesas sob pena de cancelamento da distribui&ccedil;&atilde;o.
Sem preju&iacute;zo, providencie a serventia o desentranhamento da peti&ccedil;&atilde;o de fls. 467, bem como os documentos de fls. 468/478, uma vez que estranhos aos autos.
                Intime-se.


                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                13/10/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70024777-1
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 13/10/2015 16:41

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                28/09/2015
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
                28/09/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70023289-8
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 28/09/2015 11:43

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                23/09/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0144/2015
Data da Disponibiliza&ccedil;&atilde;o: 23/09/2015
Data da Publica&ccedil;&atilde;o: 24/09/2015
N&uacute;mero do Di&aacute;rio: 1973
P&aacute;gina: 302/334
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                22/09/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0144/2015
Teor do ato: Vistos.
Fls. 453/455: Aguarde-se o julgamento do agravo.
Intime-se.


Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/09/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-23842313"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=23842313&nmRecursoAcessado=Mero+expediente">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-23842313"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=23842313&nmRecursoAcessado=Mero+expediente"> Mero expediente
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos.
Fls. 453/455: Aguarde-se o julgamento do agravo.
Intime-se.


                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                21/09/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Despacho Digitalizado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                22/07/2015
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
                22/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Despacho Digitalizado



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                15/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Pedido de Habilitação Juntado



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70015954-6
Tipo da Peti&ccedil;&atilde;o: Pedido de Habilita&ccedil;&atilde;o
Data: 15/07/2015 08:57

                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                15/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70015631-8
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 13/07/2015 14:31

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                13/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0099/2015
Data da Disponibiliza&ccedil;&atilde;o: 08/07/2015
Data da Publica&ccedil;&atilde;o: 13/07/2015
N&uacute;mero do Di&aacute;rio: 1921
P&aacute;gina: 340/346
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                08/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Decisão



                <br />
                <span style="font-style: italic;">

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                07/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0099/2015
Teor do ato: Vistos. Ciente do agravo interposto. Aguarde-se decis&atilde;o ou pedido de informa&ccedil;&otilde;es do agravo interposto. Intime-se.
Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                07/07/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-22524604"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=22524604&nmRecursoAcessado=Decis%C3%A3o">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-22524604"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=22524604&nmRecursoAcessado=Decis%C3%A3o"> Decisão
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos. Ciente do agravo interposto. Aguarde-se decis&atilde;o ou pedido de informa&ccedil;&otilde;es do agravo interposto. Intime-se.
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                30/06/2015
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
                30/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70013816-6
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&atilde;o Juntando C&oacute;pia do Agravo (Art. 526, do CPC)
Data: 23/06/2015 10:38

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                25/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0091/2015
Data da Disponibiliza&ccedil;&atilde;o: 25/06/2015
Data da Publica&ccedil;&atilde;o: 26/06/2015
N&uacute;mero do Di&aacute;rio: 1912
P&aacute;gina: 303/329
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                25/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Certidão de Publicação Expedida



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o :0091/2015
Data da Disponibiliza&ccedil;&atilde;o: 25/06/2015
Data da Publica&ccedil;&atilde;o: 26/06/2015
N&uacute;mero do Di&aacute;rio: 1912
P&aacute;gina: 303/329
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                24/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0091/2015
Teor do ato: Vistas dos autos ao autor para: (x) outros: Ci&ecirc;ncia da decis&atilde;o de fls. 385, a qual n&atilde;o foi devidamente publicada no DJE: &quot;Vistos. Indefiro o pedido de assist&ecirc;ncia judici&aacute;ria formulado pelo requerente. O benef&iacute;cio somente &eacute; concedido &agrave;s pessoas jur&iacute;dicas em situa&ccedil;&otilde;es excepcionais, visto que a pr&oacute;pria redu&ccedil;&atilde;o do artigo 2&ordm;, &sect; &uacute;nico, da Lei 1.060/50 pressup&otilde;e a sua concess&atilde;o apenas &agrave;s pessoas f&iacute;sicas. Com efeito, em se tratando de pessoa jur&iacute;dica, faz-se necess&aacute;ria a an&aacute;lise do faturamento mensal l&iacute;quido, al&eacute;m de outras provas imprescind&iacute;veis &agrave; avalia&ccedil;&atilde;o da sa&uacute;de financeira da empresa, de modo a viabilizar a exce&ccedil;&atilde;o &agrave; regra do recolhimento do valor da taxa judici&aacute;ria no momento da distribui&ccedil;&atilde;o ou, no caso de eleva&ccedil;&atilde;o do valor da causa, no momento da emenda. Assim, recolha o autor as custas necess&aacute;rias, sob pena de extin&ccedil;&atilde;o do processo. Int.&quot;
Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                24/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Remetido ao DJE



                <br />
                <span style="font-style: italic;">
                        Rela&ccedil;&atilde;o: 0091/2015
Teor do ato: Vistos. Indefiro o pedido de assist&ecirc;ncia judici&aacute;ria formulado pelo requerente. O benef&iacute;cio somente &eacute; concedido &agrave;s pessoas jur&iacute;dicas em situa&ccedil;&otilde;es excepcionais, visto que a pr&oacute;pria redu&ccedil;&atilde;o do artigo 2&ordm;, &sect; &uacute;nico, da Lei 1.060/50 pressup&otilde;e a sua concess&atilde;o apenas &agrave;s pessoas f&iacute;sicas. Com efeito, em se tratando de pessoa jur&iacute;dica, faz-se necess&aacute;ria a an&aacute;lise do faturamento mensal l&iacute;quido, al&eacute;m de outras provas imprescind&iacute;veis &agrave; avalia&ccedil;&atilde;o da sa&uacute;de financeira da empresa, de modo a viabilizar a exce&ccedil;&atilde;o &agrave; regra do recolhimento do valor da taxa judici&aacute;ria no momento da distribui&ccedil;&atilde;o ou, no caso de eleva&ccedil;&atilde;o do valor da causa, no momento da emenda. Assim, recolha o autor as custas necess&aacute;rias, sob pena de extin&ccedil;&atilde;o do processo. Int.
Advogados(s): Paula Rodrigues da Silva (OAB 221271/SP)
                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                19/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-22302171"
                                title="Visualizar documento em inteiro teor"
                                href="#liberarAutoPorSenha">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-22302171"
                                        title="Visualizar documento em inteiro teor"
                                        href="#liberarAutoPorSenha"> Ato ordinatório
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistas dos autos ao autor para: (x) outros: Ci&ecirc;ncia da decis&atilde;o de fls. 385, a qual n&atilde;o foi devidamente publicada no DJE: &quot;Vistos. Indefiro o pedido de assist&ecirc;ncia judici&aacute;ria formulado pelo requerente. O benef&iacute;cio somente &eacute; concedido &agrave;s pessoas jur&iacute;dicas em situa&ccedil;&otilde;es excepcionais, visto que a pr&oacute;pria redu&ccedil;&atilde;o do artigo 2&ordm;, &sect; &uacute;nico, da Lei 1.060/50 pressup&otilde;e a sua concess&atilde;o apenas &agrave;s pessoas f&iacute;sicas. Com efeito, em se tratando de pessoa jur&iacute;dica, faz-se necess&aacute;ria a an&aacute;lise do faturamento mensal l&iacute;quido, al&eacute;m de outras provas imprescind&iacute;veis &agrave; avalia&ccedil;&atilde;o da sa&uacute;de financeira da empresa, de modo a viabilizar a exce&ccedil;&atilde;o &agrave; regra do recolhimento do valor da taxa judici&aacute;ria no momento da distribui&ccedil;&atilde;o ou, no caso de eleva&ccedil;&atilde;o do valor da causa, no momento da emenda. Assim, recolha o autor as custas necess&aacute;rias, sob pena de extin&ccedil;&atilde;o do processo. Int.&quot;
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                19/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70013444-6
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 17/06/2015 18:15

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                11/06/2015
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
                11/06/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Petição Juntada



                <br />
                <span style="font-style: italic;">
                        N&ordm; Protocolo: WITV.15.70012875-6
Tipo da Peti&ccedil;&atilde;o: Peti&ccedil;&otilde;es Diversas
Data: 11/06/2015 14:08

                </span>

        </td>
</tr>



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                28/05/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">








                        <a class="linkMovVincProc"
                                id="linkMovVincProc-21935970"
                                title="Visualizar documento em inteiro teor"
                                href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=21935970&nmRecursoAcessado=Decis%C3%A3o">
                                <img width="16" height="16" border="0" src="/cpopg/imagens/doc2.gif" />
                        </a>

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">



                                <a class="linkMovVincProc"
                                        id="linkMovVincProc-2-21935970"
                                        title="Visualizar documento em inteiro teor"
                                        href="/cpopg/abrirDocumentoVinculadoMovimentacao.do;jsessionid=FA96050F7895436687CEF9660F8E8057.cpopg6?processo.codigo=7J0001D040000&cdDocumento=21935970&nmRecursoAcessado=Decis%C3%A3o"> Decisão
                                </a>




                <br />
                <span style="font-style: italic;">
                        Vistos. Indefiro o pedido de assist&ecirc;ncia judici&aacute;ria formulado pelo requerente. O benef&iacute;cio somente &eacute; concedido &agrave;s pessoas jur&iacute;dicas em situa&ccedil;&otilde;es excepcionais, visto que a pr&oacute;pria redu&ccedil;&atilde;o do artigo 2&ordm;, &sect; &uacute;nico, da Lei 1.060/50 pressup&otilde;e a sua concess&atilde;o apenas &agrave;s pessoas f&iacute;sicas. Com efeito, em se tratando de pessoa jur&iacute;dica, faz-se necess&aacute;ria a an&aacute;lise do faturamento mensal l&iacute;quido, al&eacute;m de outras provas imprescind&iacute;veis &agrave; avalia&ccedil;&atilde;o da sa&uacute;de financeira da empresa, de modo a viabilizar a exce&ccedil;&atilde;o &agrave; regra do recolhimento do valor da taxa judici&aacute;ria no momento da distribui&ccedil;&atilde;o ou, no caso de eleva&ccedil;&atilde;o do valor da causa, no momento da emenda. Assim, recolha o autor as custas necess&aacute;rias, sob pena de extin&ccedil;&atilde;o do processo. Int.
                </span>

        </td>
</tr>



















<tr class="fundoEscuro" style="">
        <td width="120" style="vertical-align: top">
                27/05/2015
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



















<tr class="fundoClaro" style="">
        <td width="120" style="vertical-align: top">
                26/05/2015
        </td>
        <td width="20" valign="top" aria-hidden="true">

        </td>
        <td style="vertical-align: top; padding-bottom: 5px">




                                Distribuído Livremente (por Sorteio) (movimentação exclusiva do distribuidor)



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
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Petições diversas

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                                                                11/06/2015
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                17/06/2015
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                23/06/2015
                                                        </td>
                                                        <td width="*">
                                                                Petição Juntando Cópia do Agravo (Art. 526, do CPC) <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                13/07/2015
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                15/07/2015
                                                        </td>
                                                        <td width="*">
                                                                Pedido de Habilitação <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                28/09/2015
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                13/10/2015
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                08/01/2016
                                                        </td>
                                                        <td width="*">
                                                                Petição Juntando Cópia do Agravo (Art. 526, do CPC) <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                22/01/2016
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                12/04/2016
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                01/08/2016
                                                        </td>
                                                        <td width="*">
                                                                Contestação <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                26/08/2016
                                                        </td>
                                                        <td width="*">
                                                                Manifestação Sobre a Contestação <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                01/12/2016
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                05/12/2016
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                20/03/2017
                                                        </td>
                                                        <td width="*">
                                                                Rol de Testemunha <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                23/03/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                23/03/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                04/04/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                25/04/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                09/05/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                10/05/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                10/05/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                25/05/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                30/05/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                06/11/2017
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                31/07/2018
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoClaro">
                                                        <td width="140"  style="text-align:left">
                                                                10/08/2018
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

                                                        </td>
                                                </tr>



                                                <tr class="fundoEscuro">
                                                        <td width="140"  style="text-align:left">
                                                                29/11/2018
                                                        </td>
                                                        <td width="*">
                                                                Petições Diversas <br/>

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
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Incidentes, ações incidentais, recursos e execuções de sentenças

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Apensos, Entranhados e Unificados

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
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
                <td height="21" valign="top" nowrap background="/cpopg/imagens/spw/fundo_subtitulo.gif">


                                        <h2 class="subtitle">
                                                Audiências

                                        </h2>



                </td>
                <td background="/cpopg/imagens/spw/fundo_subtitulo2.gif" width="90%" aria-hidden="true">
                        <img src="/cpopg/imagens/spw/final_subtitulo.gif" width="16" height="20" tabindex="-1">
                </td>
        </tr>
</table>



</div>
























<a name="audienciasPlaceHolder"></a>
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


                        <tr class="label">
                                <th align="left" valign="top" width="140">Data</th>
                                <th align="left" valign="top" width="*">Audiência</th>
                                <th align="left" valign="top" width="100">Situação</th>
                                <th align="left" valign="top" width="100">Qt. Pessoas</th>
                        </tr>
                        <tr class="fundoEscuro" height="2" aria-hidden="true">
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                        </tr>

                                <tr class="fundoClaro">
                                        <td valign="top" align="left" valign="top" width="140">
                                                10/05/2017
                                        </td>
                                        <td valign="top" align="left" valign="top" width="*">



                                                                Instrução e Julgamento


                                        </td>
                                        <td  align="left" valign="top" width="100">
                                                Realizada
                                        </td>
                                        <td  align="left" valign="top" width="100">
                                                5
                                        </td>
                                </tr>




</table>






























<form id="popupCdas" style="display: none;">
        <!--  dados da lista (CDAs) -->
        <div style="height:210px; overflow: auto;">
                <table id="tableCdasPrincipais" style="margin-left:10px; margin-top:1px; width: 98%;">
                        <thead>
                                <tr class="fundoClaro">
                                        <th style="text-align:left;">Número CDA</th>
                                        <th style="text-align:left;">Valor</th>
                                        <th style="text-align:left;">Dt. CDA</th>
                                        <th style="text-align:left;">Valor atualizado</th>
                                        <th style="text-align:left;">Dt. atualização</th>
                                        <th style="text-align:left;">Situação</th>
                                </tr>
                                <tr class="fundoEscuro" height="2" aria-hidden="true">
                                        <td colspan="6"/>
                                </tr>
                        </thead>
                        <tbody>

                        </tbody>
                </table>
        </div>
</form>

















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
            Desenvolvido pela Softplan em parceria com a Secretaria de Tecnologia da Informação - STI

        </td>
    </tr>
</table>
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/saj-popup-modal.css" rel="stylesheet" type="text/css">
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/popup-beta.css" rel="stylesheet" type="text/css">



<script>
    appEsajLayout = {
        botaoNovaVersao: 'Ir para nova versão',
        botaoVersaoAnterior: 'Ir para versão anterior',
        tituloNovaVersao: 'Nova versão do Portal e-SAJ!',
        tituloVersaoAnterior: 'Versão anterior',
        tituloCertificadoDigital: 'Certificado digital',
        cliente: 'SP',

        emailParaContato: 'esajtjsp@softplan.com.br',
        utilizarBotaoContato: 'true',
        contexto: 'https://esaj.tjsp.jus.br/esaj'
    };
    if(window.jQuery) {
        jQuery.saj = jQuery.saj || {};
        jQuery.saj.certificado = jQuery.saj.certificado || {};
        jQuery.saj.certificado.cliente = 'SP';
        jQuery.saj.certificado.tituloCertificadoDigital = 'Certificado digital';
        jQuery.saj.certificado.tituloProblemasAoAssinar = 'Falha de comunicação com o dispositivo de assinatura digital';
        jQuery.saj.certificado.urlConteudoAjudaWebSigner = appEsajLayout.contexto + '/ajudaWebSigner.do';
        jQuery.saj.certificado.licenca = 'ARkEKi50anNwLmp1cy5iciwxMC4zMy4xOTIuMTAxLDEwLjMzLjE5Mi4xMDUsMTAuMzMuMTkyLjE0NiwxMC4zMy4xOTIuMjQxLDEwLjMzLjE5Mi45MCwxMC4zMy4xOTIuOTEsMTAuMzMuMTkyLjkyLDEwLjMzLjE5Mi45NCwxMC4zMy4xOTMuMTg1LDEwLjMzLjE5My4xODYsMTAuMzMuMTkzLjE4NywxMC4zMy4xOTMuMTg4LDEwLjMzLjE5NC4yMjQsMTAuMzMuMTk0LjIyNSwxMC4zMy4xOTQuMjU1LDEwLjMzLjE5NC43NCwxMC4zMy4xOTQuNzUsMTAuMzMuMTk0Ljc2LDEwLjMzLjE5NC43NywxMC4zMy4xOTQuNzksMTAuMzMuMTk1LjEwMiwxMC4zMy4xOTUuMTAyLDEwLjMzLjE5NS4xMTksMTAuMzMuMTk1LjEyMSwxMC4zMy4xOTUuMTIyLDEwLjMzLjE5NS4xMjMsMTAuMzMuMTk1LjEyNCwxMC4zMy4xOTUuMTI1LDEwLjMzLjE5NS4xMjYsMTAuMzMuMTk1LjEyNywxMC4zMy4xOTUuMTI4LDEwLjMzLjE5NS4xMjksMTAuMzMuMTk1LjEzMCwxMC4zMy4xOTUuMTMxLDEwLjMzLjE5NS4xMzIsMTAuMzMuMTk1LjE4MywxMC4zMy4xOTUuMTg0LDEwLjMzLjE5NS4xODUsMTAuMzMuMTk1LjE4NiwxMC4zMy4xOTUuMTg3LDEwLjMzLjE5NS4xODgsMTAuMzMuMTk1LjE4OSwxMC4zMy4xOTUuMTkxLDEwLjMzLjE5NS4xOTIsMTAuMzMuMTk1LjE5MywxMC4zMy4xOTUuMTk0LDEwLjMzLjE5NS4xOTUsMTAuMzMuMTk1LjE5NSwxMC4zMy4xOTUuMTk3LDEwLjMzLjE5NS4xOTgsMTAuMzMuMTk1LjIzNCwxMC4zMy4xOTUuMjM3LDEwLjk4LjE5Mi4xMTMsMTAuOTguMTkyLjExNCwxMC45OC4xOTIuMTE3LDEwLjk4LjE5Mi4yNTAsMTAuOTguMTkyLjQyLDEwLjk4LjE5Mi43MCwxMC45OC4xOTIuNzEsMTAuOTguMTkzLjEyMSwxMC45OC4xOTMuMTIyLDEwLjk4LjE5My4xOTksMTAuOTguMTkzLjIwMCwxMC45OC4xOTMuMjAxLDEwLjk4LjE5My4yMDIsMTAuOTguMTkzLjIyNSwxMC45OC4xOTQuMTIxLDEwLjk4LjE5NC4xMjIsMTAuOTguMTk0LjE0MSwxMC45OC4xOTQuMTQyLDEwLjk4LjE5NC4xNDMsMTAuOTguMTk0LjE0NCwxMC45OC4xOTQuMTQ1LDEwLjk4LjE5NC4xNDcsMTAuOTguMzIuNzYAAAABt8T6Ov8g0lWHnOe7bekYQC1kjn/SgVPWGteqlpMDF8qEOKOxdWahBlk0uh9nfmPiUY9MXcXchlgu6V/zygYGgSfZG11odlUkrXZCAYX/pB3ArsqmrqgvMK0mxuTVOThs/flGWltXnCFEFEU1Pp6RSdlhtCOEuGx5XWov3lux8DcnB+DxL2zauU4GfGJmoXCZDMWT2g7MXIu7VjrJJEkCH/nZ0hkhUsw/k0ORu7/kXJyBufrFZYbsQ/Nadjp9CgYhlsjKXmSPSn8GU8xUetHXGX3FzFJriyk8iqcH72p4z0/Msif4S+VNz0JV3+xffRvdmKuG28jHHDUqBxIrhjs+XA==';
        jQuery.saj.certificado.cofreDigital = jQuery.saj.certificado.cofreDigital || {};
        jQuery.saj.certificado.cofreDigital.habilitado = 'false' === 'true';
        jQuery.saj.certificado.cofreDigital.enderecoBase = 'https://esaj.tjsp.jus.br/esaj';
    }

</script>
<script src="https://esaj.tjsp.jus.br/esaj/js/app-bundle.js?n=2830363862"></script>
<script language="javascript" type="text/JavaScript" src="https://websigner.softplan.com.br/Content/js/softplan-websigner-2.5.0.js?n=62fddc48-c657-4f9b-95db-73bb59e7bb4b"></script>

<script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/esaj/js/saj-certificado.js?n=2205257179"></script>



<div id="webSignerNaoInstalado" style="display: none;">
    <p>Para utilização do certificado digital no Portal e-SAJ é necessário a instalação do plug-in Web Signer. Por favor, realize a instalação antes de continuar.</p>
    <div class="footer_certificado">
        <button id="redirecionarParaPaginaInstalacao" class="actionPrincipal spwBotaoDefault">Instalar</button>
        <button class="fecharModalInstalacao spwBotao">Cancelar</button>
        <button class="spwBotao" onclick="window.open('https://esaj.tjsp.jus.br/WebHelp//#id_instalacao_lacuna.htm','_blank')">Ajuda</button>
    </div>
</div>

<div id="webSignerNaoSuportado" style="display: none;">
    <p>O navegador utilizado não é compatível com a tecnologia (Web Signer) necessária para utilização do certificado digital. Por favor, utilize um dos navegadores homologados. Em caso de dúvidas, efetue a validação de requisitos <a href="https://esaj.tjsp.jus.br/petpg/abrirVerificacaoRequisitosPet.do" target="_blank">aqui</a>.</p>
    <div class="footer_certificado">
        <button class="fecharModalInstalacao spwBotaoDefault actionPrincipal">OK</button>
    </div>
</div>



























        <form action="/cpopg/show.do?processo.codigo=7J0001D040000&processo.foro=271" id="popupSenha" style="display: none;" method="POST">

                <table>


                                        <tr>
                                                <td colspan="2" style="padding-left: 20px" class="orientacao121" tabindex="2" aria-label="Atendendo o que está exposto na Res. 121 do CNJ.">
                                                        Atendendo o que está exposto na Res. 121 do CNJ.
                                                </td>
                                        <tr>
                                        <tr>
                                                <td colspan="2" tabindex="3" aria-label="Será necessário informar uma senha para acessar processos em segredo de justiça, bem como para acessar autos dos demais processos. Caso não a possua e seja parte do processo, dirija-se ao cartório para solicitá-la.">
                                                <img src="/cpopg/imagens/setaTopico.gif">
                                                Será necessário informar uma senha para acessar processos em segredo de justiça, bem como para acessar autos dos demais processos. Caso não a possua e seja parte do processo, dirija-se ao cartório para solicitá-la.</td>
                                        </tr>
                                        <tr>
                                                <td colspan="2" tabindex="4" aria-label="Se for advogado (a) neste processo habilite-se no Portal ou efetue login pelo link "Identificar-se". O número de sua OAB no cadastro do Portal deverá ser igual ao número nos dados do processo.">
                                                <img src="/cpopg/imagens/setaTopico.gif">
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

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":451,"applicationID":"213910891","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfTxZHQRZCFkpRAkNZXw9LYFsMQSQHRAhYXg==","queueTime":0}</script></body>
</html>
"""
