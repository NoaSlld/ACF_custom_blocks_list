<?php
$image = $block['image'];
$isLogo = $block['is-link'];
$link = $block['link'];
$title = $block['title'];
$description = $block['description'];
$display_button = $block['display_button'];
$button = $block['button'];
$button_logo = $block['text_image_button_logo'];
$display_separator = $block['display_separator'];
$reverse_columns = $block['reverse_columns'];
$margins = $block['margins'];
$blue_background = $block['blue_background'];
$round_upper_right_corner = $block['round_upper_right_corner'];
$round_upper_left_corner = $block['round_upper_left_corner'];
$shift_top = $block['shift_top'];
?>


<section class="block--text-image
    <?php echo $blue_background ? 'blue-background' : ''; ?>
    <?php echo $round_upper_left_corner ? 'round-upper-left' : ''; ?>
    <?php echo $round_upper_right_corner ? 'round-upper-right' : ''; ?>" style="<?php
           echo isset($margins['margin-top']) && !empty($margins['margin-top']) ? 'margin-top: ' . $margins['margin-top'] . 'px;' : '';
           echo isset($margins['margin-bottom']) && !empty($margins['margin-bottom']) ? 'padding-bottom: ' . $margins['margin-bottom'] . 'px;' : '';
           ?>">
    <div class="large-container <?php echo $reverse_columns ? 'reverse-columns' : ''; ?> ">
        <div class="content">

            <?php if (!empty($title)): ?>
                <h2 class="htitle with-return"><?php echo $title; ?></h2>
            <?php endif; ?>

            <?php if ($display_separator == true): ?>
                <span class='separator'></span>
            <?php endif; ?>

            <?php if (!empty($description)): ?>
                <div class="description"> <?php echo $description; ?> </div>
            <?php endif; ?>

            <?php if (!empty($button['url']) && $display_button): ?>
                <div class="link-container">
                    <a class="btn primary-btn <?php echo !empty($button_logo) ? 'btn-with-logo' : ''; ?>"
                        href="<?php echo $button['url']; ?>"
                        target="<?php echo $button['target']; ?>"><?php echo $button['title']; ?>
                        <?php if (!empty($button_logo)): ?>
                            <div class="btn-img-container">
                                <?php echo wp_get_attachment_image($button_logo, 'full', false, ['draggable' => false, 'loading' => 'lazy']); ?>
                            </div>
                        <?php endif; ?>
                    </a>
                </div>
            <?php endif; ?>

        </div>

        <?php if ($image): ?>
            <?php if ($isLogo && !empty($link)): ?>
                <a href="<?php echo $link; ?>" class="logo-container">
                    <?php echo wp_get_attachment_image($image, 'full', false, ['draggable' => false, 'loading' => 'lazy']); ?>
                </a>
            <?php else: ?>
                <div class="image-container <?php echo $shift_top ? 'shift-top' : ''; ?> ">
                    <?php echo wp_get_attachment_image($image, 'full', false, ['draggable' => false, 'loading' => 'lazy']); ?>
                </div>
            <?php endif; ?>
        <?php endif; ?>

    </div>
</section>