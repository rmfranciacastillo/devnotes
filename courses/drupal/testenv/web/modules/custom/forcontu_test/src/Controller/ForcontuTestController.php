<?php

namespace Drupal\forcontu_test\Controller;

use Drupal\Core\Controller\ControllerBase;

/**
 * Returns responses for Forcontu test routes.
 */
class ForcontuTestController extends ControllerBase {

  /**
   * Builds the response.
   */
  public function build() {

    $build['content'] = [
      '#type' => 'item',
      '#markup' => $this->t('It works!'),
    ];

    return $build;
  }

}
