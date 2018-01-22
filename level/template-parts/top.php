<div class="off-canvas-wrapper" >
<div class="off-canvas-wrapper-inner"  data-off-canvas-wrapper>
<div class="off-canvas position-left" id="offCanvas" data-off-canvas>
 <?php  
   get_search_form();
   ?> 
   
<?php 
$offcanvasnav = array(
	'theme_location'  => 'mobile',
	'container'       => 'div',
	'menu_class'      => 'menu',
	'menu_id'         => 'mobile-menu',
	'echo'            => true,
	'fallback_cb'     => 'wp_page_menu',
	'items_wrap'      => '<ul id="%1$s" class="%2$s vertical data-drilldown">%3$s</ul>',
	//'depth'           => 1,
);
wp_nav_menu( $offcanvasnav ); // navigation of you website ?> 
</div>
<div class="title-bar" data-responsive-toggle="sand"  data-off-canvas-content data-hide-for="large">
<span type="button" data-toggle="offCanvas"><ul class="menu"> <li><span class="levelmobmenu"></span></li>
<li><span class="levelmoblogo">

 <?php if ( level_the_custom_logo()  ) {
      level_the_custom_logo();   }
   else { if ( is_front_page() && is_home() ) : ?>
		<h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
	<?php else : ?>
		<p class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></p>
	<?php endif; }  ?>  </span></li>
<li> <span class="levelmobsearch"></span>
</li></span>
</div>


<div class="floatingmenu">
<div class="row">
<div class="large-6 columns logo">
 <?php if ( level_the_custom_logo()  ) {
      level_the_custom_logo();   }
   else { if ( is_front_page() && is_home() ) : ?>
		<h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
	<?php else : ?>
		<p class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></p>
	<?php endif; }  ?>  
   
</div>
  <div class="large-8 columns">  <nav id="site-navigation" class="main-navigation" role="navigation" itemscope itemtype="http://schema.org/SiteNavigationElement">
			<button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false"><?php esc_html_e( 'Primary Menu', 'level' ); ?></button>
			<?php wp_nav_menu( array( 'theme_location' => 'primary', 'menu_id' => 'primary-menu'
			//,'walker' => new level_Walker_Nav_Menu() 
			) ); ?>
		</nav><!-- #site-navigation --></div>
  <div class="large-2 columns socialicon">
  <?php
  
	get_search_form();

  ?>
  
 <?php //if(of_get_option('level_topmenusearch') !=='hide'){ get_search_form(); } ?>
</div>
</div>
</div>


