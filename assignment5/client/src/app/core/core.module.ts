import { NgModule, Optional, SkipSelf, ErrorHandler } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { MediaMatcher } from '@angular/cdk/layout';
import { NGXLogger } from 'ngx-logger';

import { AuthInterceptor } from './interceptors/auth.interceptor';
import { SpinnerInterceptor } from './interceptors/spinner.interceptor';
import { AuthGuard } from './guards/auth/auth.guard';
import { throwIfAlreadyLoaded } from './guards/module-import.guard';
import { GlobalErrorHandler } from './services/httpErrorHandler/globar-error.handler';
import { AdminGuard } from './guards/admin/admin.guard';
import { ChartModule } from '../shared/charts/chart.module';

@NgModule({
  imports: [CommonModule, HttpClientModule,ChartModule],
  declarations: [],
  providers: [
    AuthGuard,
    AdminGuard,
    MediaMatcher,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: SpinnerInterceptor,
      multi: true,
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    },
    {
      provide: ErrorHandler,
      useClass: GlobalErrorHandler,
    },
    { provide: NGXLogger, useClass: NGXLogger },
    { provide: 'LOCALSTORAGE', useValue: window.localStorage },
  ],
  exports: [],
})
export class CoreModule {
  constructor(@Optional() @SkipSelf() parentModule: CoreModule) {
    throwIfAlreadyLoaded(parentModule, 'CoreModule');
  }
}
